import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from collections import Counter

# Set style for plots
plt.style.use('ggplot')
sns.set(font_scale=1.2)
sns.set_style("whitegrid")

# Read the dataset
df = pd.read_csv('../Dataset/dataset.csv')

# Save basic statistics
def save_basic_stats():
    # Sample size
    total_participants = len(df)
    
    # Age distribution
    age_distribution = df['Age Group'].value_counts().sort_index()
    
    # Role distribution
    role_distribution = df['Primary Role'].value_counts()
    
    # Education distribution
    education_distribution = df['Education'].value_counts().sort_values(ascending=False)
    
    # Experience distribution
    experience_distribution = df['Coding Experience'].value_counts().sort_index()
    
    # Most used programming languages
    languages = []
    for lang in df['Most Frequent Languages']:
        languages.append(lang)
    
    language_counts = Counter(languages)
    
    # Usage frequency
    usage_frequency = df['AI Tool Usage Frequency'].value_counts().sort_index()
    
    # Tools used
    tools = []
    for tool_list in df['AI Tools Used']:
        for tool in tool_list.split(' and '):
            tools.append(tool.strip())
    
    tool_counts = Counter(tools)
    
    # Create a stats text file
    with open('analysis_stats.txt', 'w') as f:
        f.write(f"Total participants: {total_participants}\n\n")
        
        f.write("Age Distribution:\n")
        for age, count in age_distribution.items():
            f.write(f"{age}: {count} ({count/total_participants*100:.1f}%)\n")
        
        f.write("\nPrimary Role Distribution:\n")
        for role, count in role_distribution.items():
            f.write(f"{role}: {count} ({count/total_participants*100:.1f}%)\n")
        
        f.write("\nEducation Distribution:\n")
        for edu, count in education_distribution.items():
            f.write(f"{edu}: {count} ({count/total_participants*100:.1f}%)\n")
        
        f.write("\nCoding Experience Distribution:\n")
        for exp, count in experience_distribution.items():
            f.write(f"{exp}: {count} ({count/total_participants*100:.1f}%)\n")
        
        f.write("\nMost Used Programming Languages:\n")
        for lang, count in language_counts.most_common():
            f.write(f"{lang}: {count} ({count/total_participants*100:.1f}%)\n")
        
        f.write("\nAI Tool Usage Frequency:\n")
        for freq, count in usage_frequency.items():
            f.write(f"{freq}: {count} ({count/total_participants*100:.1f}%)\n")
        
        f.write("\nAI Tools Used:\n")
        for tool, count in tool_counts.most_common():
            f.write(f"{tool}: {count} ({count/total_participants*100:.1f}%)\n")

# Create visualizations
def create_visualizations():
    # Create output directory for plots
    import os
    if not os.path.exists('plots'):
        os.makedirs('plots')
    
    # 1. Age distribution
    plt.figure(figsize=(10, 6))
    sns.countplot(y=df['Age Group'], order=sorted(df['Age Group'].unique()))
    plt.title('Distribution of Participants by Age Group')
    plt.tight_layout()
    plt.savefig('plots/age_distribution.png', dpi=300)
    plt.close()
    
    # 2. Primary role distribution
    plt.figure(figsize=(12, 6))
    role_counts = df['Primary Role'].value_counts()
    sns.barplot(x=role_counts.index, y=role_counts.values)
    plt.title('Distribution of Primary Roles')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('plots/role_distribution.png', dpi=300)
    plt.close()
    
    # 3. Programming Languages
    plt.figure(figsize=(12, 6))
    language_counts = df['Most Frequent Languages'].value_counts().head(10)
    sns.barplot(x=language_counts.index, y=language_counts.values)
    plt.title('Top 10 Programming Languages Used')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('plots/language_distribution.png', dpi=300)
    plt.close()
    
    # 4. AI Tools Used
    tools = []
    for tool_list in df['AI Tools Used']:
        for tool in tool_list.split(' and '):
            tools.append(tool.strip())
    
    tool_counts = Counter(tools)
    plt.figure(figsize=(12, 6))
    tool_df = pd.DataFrame(tool_counts.most_common(), columns=['Tool', 'Count'])
    sns.barplot(x='Tool', y='Count', data=tool_df)
    plt.title('AI Tools Used by Participants')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('plots/tools_used.png', dpi=300)
    plt.close()
    
    # 5. AI Usage Frequency
    plt.figure(figsize=(10, 6))
    order = ['Daily', 'Weekly', 'Occasionally', 'No Change']
    sns.countplot(y=df['AI Tool Usage Frequency'], order=order)
    plt.title('AI Tool Usage Frequency')
    plt.tight_layout()
    plt.savefig('plots/usage_frequency.png', dpi=300)
    plt.close()
    
    # 6. Coding Speed Impact
    plt.figure(figsize=(10, 6))
    order = ['Significantly Increased', 'Slightly Increased', 'No Change']
    sns.countplot(y=df['Coding Speed Impact'], order=order)
    plt.title('Impact on Coding Speed')
    plt.tight_layout()
    plt.savefig('plots/coding_speed_impact.png', dpi=300)
    plt.close()
    
    # 7. Code Quality Impact
    plt.figure(figsize=(10, 6))
    order = ['Improved significantly', 'Improved slightly', 'No change']
    sns.countplot(y=df['Code Quality Impact'], order=order)
    plt.title('Impact on Code Quality')
    plt.tight_layout()
    plt.savefig('plots/code_quality_impact.png', dpi=300)
    plt.close()
    
    # 8. AI Primary Use
    plt.figure(figsize=(12, 6))
    primary_use_counts = df['AI Coding Primary Use'].value_counts()
    sns.barplot(x=primary_use_counts.index, y=primary_use_counts.values)
    plt.title('Primary Use of AI Coding Tools')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('plots/primary_use.png', dpi=300)
    plt.close()
    
    # 9. AI Code Trust Level
    plt.figure(figsize=(10, 6))
    sns.countplot(y=df['AI Code Trust Level'])
    plt.title('Trust Level in AI-generated Code (1-5 scale)')
    plt.tight_layout()
    plt.savefig('plots/trust_level.png', dpi=300)
    plt.close()
    
    # 10. AI Coding Concerns
    plt.figure(figsize=(12, 6))
    concerns_counts = df['AI Coding Concerns'].value_counts()
    sns.barplot(x=concerns_counts.index, y=concerns_counts.values)
    plt.title('Concerns About AI Coding Tools')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('plots/concerns.png', dpi=300)
    plt.close()
    
    # 11. AI Replacement Perception
    plt.figure(figsize=(12, 6))
    replacement_counts = df['AI Replacement Perception'].value_counts()
    sns.barplot(x=replacement_counts.index, y=replacement_counts.values)
    plt.title('Perceptions on AI Replacing Developers')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('plots/replacement_perception.png', dpi=300)
    plt.close()
    
    # 12. AI Creativity Impact
    plt.figure(figsize=(12, 6))
    creativity_counts = df['Creativity Impact'].value_counts()
    sns.barplot(x=creativity_counts.index, y=creativity_counts.values)
    plt.title('Impact on Creativity')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('plots/creativity_impact.png', dpi=300)
    plt.close()

# Create crosstab analysis
def create_crosstab_analysis():
    # Age vs AI Trust Level
    age_trust = pd.crosstab(df['Age Group'], df['AI Code Trust Level'], normalize='index') * 100
    age_trust.to_csv('age_vs_trust.csv')
    
    # Role vs AI Usage Frequency
    role_usage = pd.crosstab(df['Primary Role'], df['AI Tool Usage Frequency'], normalize='index') * 100
    role_usage.to_csv('role_vs_usage.csv')
    
    # Role vs Coding Speed Impact
    role_speed = pd.crosstab(df['Primary Role'], df['Coding Speed Impact'], normalize='index') * 100
    role_speed.to_csv('role_vs_speed.csv')
    
    # Experience vs AI Trust Level
    exp_trust = pd.crosstab(df['Coding Experience'], df['AI Code Trust Level'], normalize='index') * 100
    exp_trust.to_csv('experience_vs_trust.csv')
    
    # Trust vs Coding Speed Impact
    trust_speed = pd.crosstab(df['AI Code Trust Level'], df['Coding Speed Impact'], normalize='index') * 100
    trust_speed.to_csv('trust_vs_speed.csv')
    
    # Experience vs AI Replacement Perception
    exp_replace = pd.crosstab(df['Coding Experience'], df['AI Replacement Perception'], normalize='index') * 100
    exp_replace.to_csv('experience_vs_replacement.csv')
    
    # Role vs AI Coding Concerns
    role_concerns = pd.crosstab(df['Primary Role'], df['AI Coding Concerns'], normalize='index') * 100
    role_concerns.to_csv('role_vs_concerns.csv')

# Analyze trending software requests
def analyze_software_requests():
    # Extract the software requests
    software_requests = df['Autonomous Software Request'].tolist()
    
    # Categorize the requests
    categories = {
        'development_tools': ['project management', 'code', 'refactoring', 'architect', 'design system', 'workflow', 'API', 'documentation'],
        'learning_tools': ['learning', 'tutorial', 'visualization', 'educational', 'teaching', 'curriculum', 'skills', 'interview'],
        'data_analysis': ['data analysis', 'analytics', 'visualization', 'prediction', 'forecasting', 'anomaly', 'models'],
        'research_tools': ['research', 'paper', 'academic', 'literature', 'citation', 'scientific', 'hypothesis'],
        'security': ['security', 'secure', 'trust', 'protection'],
        'specialized_systems': ['healthcare', 'financial', 'legacy', 'maintenance']
    }
    
    # Count occurrences
    categorized_counts = {category: 0 for category in categories}
    
    for request in software_requests:
        request_lower = request.lower()
        for category, keywords in categories.items():
            if any(keyword in request_lower for keyword in keywords):
                categorized_counts[category] += 1
    
    # Create visualization
    plt.figure(figsize=(12, 6))
    categories_df = pd.DataFrame(list(categorized_counts.items()), columns=['Category', 'Count'])
    sns.barplot(x='Category', y='Count', data=categories_df)
    plt.title('Categories of Requested Autonomous Software')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('plots/software_request_categories.png', dpi=300)
    plt.close()
    
    # Save to file
    with open('software_requests_analysis.txt', 'w') as f:
        f.write("Software Request Categories:\n")
        for category, count in categorized_counts.items():
            f.write(f"{category}: {count} ({count/len(software_requests)*100:.1f}%)\n")
        
        f.write("\nSample requests by category:\n")
        for category, keywords in categories.items():
            f.write(f"\n{category.upper()}:\n")
            count = 0
            for request in software_requests:
                request_lower = request.lower()
                if any(keyword in request_lower for keyword in keywords) and count < 5:
                    f.write(f"- {request}\n")
                    count += 1

if __name__ == "__main__":
    save_basic_stats()
    create_visualizations()
    create_crosstab_analysis()
    analyze_software_requests()
    print("Analysis complete. Check the output files for results.") 