import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import nltk
import re
from wordcloud import WordCloud
import os

# Create plots directory if it doesn't exist
if not os.path.exists('plots'):
    os.makedirs('plots')

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

# Get stopwords
stop_words = set(nltk.corpus.stopwords.words('english'))

# Read the dataset
df = pd.read_csv('../Dataset/dataset.csv')

# Define the open-ended questions to analyze
open_ended_columns = [
    'Desired Improvements',
    'Additional Comments',
    'Autonomous Software Request'
]

# Preprocess text function with simpler tokenization
def preprocess_text(text):
    """Clean and preprocess text data."""
    if not isinstance(text, str):
        return ""
    
    # Convert to lowercase
    text = text.lower()
    
    # Simple tokenization using regex
    tokens = re.findall(r'\b\w+\b', text)
    
    # Remove stopwords
    tokens = [token for token in tokens if token not in stop_words]
    
    # Join tokens back to string
    return " ".join(tokens)

# Function to perform k-means clustering on column
def perform_kmeans_clustering(column_name):
    print(f"Performing K-means clustering on '{column_name}'...")
    
    # Get the column data and preprocess
    texts = df[column_name].fillna("").apply(preprocess_text)
    
    # Vectorize the text data
    vectorizer = TfidfVectorizer(max_features=100)
    X = vectorizer.fit_transform(texts)
    
    # Find optimal number of clusters using silhouette score
    silhouette_scores = []
    max_clusters = min(10, X.shape[0] - 1)  # Ensure we don't try more clusters than data points
    K_range = range(2, max_clusters + 1)
    
    for k in K_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        cluster_labels = kmeans.fit_predict(X)
        
        # Calculate silhouette score
        score = silhouette_score(X, cluster_labels)
        silhouette_scores.append(score)
        print(f"  Clusters: {k}, Silhouette Score: {score:.4f}")
    
    # Find the optimal k
    optimal_k = K_range[np.argmax(silhouette_scores)]
    print(f"  Optimal number of clusters: {optimal_k}")
    
    # Plot silhouette scores
    plt.figure(figsize=(10, 6))
    plt.plot(list(K_range), silhouette_scores, 'bo-')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Silhouette Score')
    plt.title(f'Silhouette Score for {column_name}')
    plt.grid(True)
    plt.savefig(f'plots/silhouette_score_{column_name.lower().replace(" ", "_")}.png', dpi=300)
    
    # Perform K-means with optimal number of clusters
    kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
    df[f'{column_name} Cluster'] = kmeans.fit_predict(X)
    
    # Reduce dimensionality to 2D for visualization
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(X.toarray())
    
    # Create a scatter plot
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(pca_result[:, 0], pca_result[:, 1], c=df[f'{column_name} Cluster'], cmap='viridis', alpha=0.7)
    plt.colorbar(scatter)
    plt.title(f'Cluster Visualization for {column_name}')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.savefig(f'plots/cluster_scatter_{column_name.lower().replace(" ", "_")}.png', dpi=300)
    
    # Create word clouds for each cluster
    for cluster_id in range(optimal_k):
        cluster_texts = texts[df[f'{column_name} Cluster'] == cluster_id]
        if len(cluster_texts) > 0:
            combined_text = ' '.join(cluster_texts)
            try:
                wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=50).generate(combined_text)
                
                plt.figure(figsize=(10, 6))
                plt.imshow(wordcloud, interpolation='bilinear')
                plt.axis('off')
                plt.title(f'{column_name} - Cluster {cluster_id + 1} WordCloud')
                plt.savefig(f'plots/{column_name.lower().replace(" ", "_")}_cluster_{cluster_id + 1}_wordcloud.png', dpi=300)
            except ValueError as e:
                print(f"Could not generate wordcloud for cluster {cluster_id}: {e}")
    
    # Summarize most frequent words per cluster
    cluster_summaries = []
    feature_names = vectorizer.get_feature_names_out()
    
    # Get cluster centers and find the top terms for each cluster
    for i, center in enumerate(kmeans.cluster_centers_):
        # Sort the center's feature values in descending order
        sorted_indices = center.argsort()[::-1]
        # Get the top 5 words
        top_terms = [feature_names[idx] for idx in sorted_indices[:5]]
        cluster_summaries.append({
            'Cluster': i + 1,
            'Count': sum(df[f'{column_name} Cluster'] == i),
            'Top Terms': ', '.join(top_terms)
        })
    
    # Create a dataframe from the summaries
    cluster_summary_df = pd.DataFrame(cluster_summaries)
    print("\nCluster Summaries:")
    print(cluster_summary_df)
    
    # Plot the frequency of each cluster
    plt.figure(figsize=(10, 6))
    counts = df[f'{column_name} Cluster'].value_counts().sort_index()
    sns.barplot(x=counts.index, y=counts.values)
    plt.xlabel('Cluster')
    plt.ylabel('Count')
    plt.title(f'Frequency of Clusters for {column_name}')
    plt.savefig(f'plots/cluster_frequency_{column_name.lower().replace(" ", "_")}.png', dpi=300)
    
    return cluster_summary_df

# Perform clustering for each open-ended question
cluster_summaries = {}
for column in open_ended_columns:
    cluster_summaries[column] = perform_kmeans_clustering(column)

# Analyze the relationship between clusters and other variables
def analyze_cluster_relationships(column_name):
    print(f"\nAnalyzing relationships for {column_name} clusters...")
    
    # Check relationship with Primary Role
    role_cluster_crosstab = pd.crosstab(
        df['Primary Role'], 
        df[f'{column_name} Cluster'],
        normalize='index'
    ) * 100
    
    # Plot heatmap of Role vs Cluster
    plt.figure(figsize=(12, 8))
    sns.heatmap(role_cluster_crosstab, annot=True, cmap='YlGnBu', fmt='.1f')
    plt.title(f'Primary Role vs {column_name} Clusters (%)')
    plt.savefig(f'plots/role_vs_{column_name.lower().replace(" ", "_")}_cluster_heatmap.png', dpi=300)
    
    # Check relationship with Experience
    exp_cluster_crosstab = pd.crosstab(
        df['Coding Experience'], 
        df[f'{column_name} Cluster'],
        normalize='index'
    ) * 100
    
    # Plot heatmap of Experience vs Cluster
    plt.figure(figsize=(12, 8))
    sns.heatmap(exp_cluster_crosstab, annot=True, cmap='YlGnBu', fmt='.1f')
    plt.title(f'Coding Experience vs {column_name} Clusters (%)')
    plt.savefig(f'plots/experience_vs_{column_name.lower().replace(" ", "_")}_cluster_heatmap.png', dpi=300)
    
    # Check relationship with Trust Level
    trust_cluster_crosstab = pd.crosstab(
        df['AI Code Trust Level'], 
        df[f'{column_name} Cluster'],
        normalize='index'
    ) * 100
    
    # Plot heatmap of Trust Level vs Cluster
    plt.figure(figsize=(12, 8))
    sns.heatmap(trust_cluster_crosstab, annot=True, cmap='YlGnBu', fmt='.1f')
    plt.title(f'AI Trust Level vs {column_name} Clusters (%)')
    plt.savefig(f'plots/trust_vs_{column_name.lower().replace(" ", "_")}_cluster_heatmap.png', dpi=300)

# Analyze relationships for each column
for column in open_ended_columns:
    analyze_cluster_relationships(column)

# Export the results to a text file
def export_cluster_summaries():
    with open('kmeans_clustering_results.txt', 'w') as f:
        f.write("K-Means Clustering Analysis of Open-Ended Questions\n")
        f.write("==================================================\n\n")
        
        for column in open_ended_columns:
            f.write(f"\n{column} Clustering Results:\n")
            f.write("-" * (len(column) + 20) + "\n")
            f.write(f"Number of clusters: {len(cluster_summaries[column])}\n\n")
            f.write(cluster_summaries[column].to_string(index=False))
            f.write("\n\n")
            
            # Add examples from each cluster
            f.write("Example entries from each cluster:\n")
            for i in range(len(cluster_summaries[column])):
                f.write(f"\nCluster {i+1} examples:\n")
                examples = df[df[f'{column} Cluster'] == i][column].head(3).tolist()
                for j, example in enumerate(examples):
                    f.write(f"  {j+1}. {example}\n")
            f.write("\n" + "=" * 50 + "\n")

# Export the summaries
export_cluster_summaries()

print("\nK-means clustering analysis complete. Results saved to 'kmeans_clustering_results.txt'")
print("Visualizations saved to the 'plots' directory.") 