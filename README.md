# AI Coding Tools Impact Analysis

This repository contains data analysis and research on the impact of AI coding tools on developer productivity and perception. The project analyzes survey data from 97 professionals with diverse backgrounds to understand usage patterns, perceptions, and concerns related to AI coding tools.

## Repository Structure

### `/Dataset`
Contains the raw survey data used for the analysis:
- `dataset.csv` - Survey responses from 97 participants, including demographics, AI tool usage patterns, impacts, and perceptions

### `/analysis`
Contains the code and intermediate outputs from the data analysis process:
- `data_analysis.py` - Python script that performs statistical analysis and generates visualizations
- `kmeans_clustering.py` - Python script that applies K-means clustering to open-ended question responses
- `kmeans_clustering_results.txt` - Results of the K-means clustering analysis with cluster summaries
- `analysis_stats.txt` - Basic descriptive statistics about the survey respondents
- `software_requests_analysis.txt` - Analysis of requested autonomous software capabilities
- Cross-tabulation analysis files (CSV format):
  - `age_vs_trust.csv` - Relationship between age groups and trust levels
  - `role_vs_usage.csv` - AI tool usage frequency by professional role
  - `role_vs_speed.csv` - Coding speed impact by professional role
  - `experience_vs_trust.csv` - Relationship between experience level and AI trust
  - `trust_vs_speed.csv` - Impact of trust levels on coding speed
  - `experience_vs_replacement.csv` - AI replacement perceptions by experience level
  - `role_vs_concerns.csv` - AI concerns by professional role
- `/plots` subdirectory - Visualizations generated from the data analysis, including:
  - Demographic distributions
  - AI tool usage patterns
  - Impact on productivity and code quality
  - Trust levels and concerns
  - Creativity impact
  - Future software capabilities
  - K-means clustering visualizations (PCA plots, wordclouds, heatmaps)

### `/final_research`
Contains the final research outputs and presentation materials:
- `research_paper.md` - Markdown version of the research paper with findings and discussion
- Analysis results and visualizations for presentation

### Project Root
- `research_paper.tex` - Complete LaTeX version of the research paper, professional-grade with formatted tables, figures, and bibliography
- `build_paper.bat` - Windows batch script to compile the LaTeX document
- `build_paper.sh` - Unix/Linux/Mac shell script to compile the LaTeX document
- `README.md` - This file, providing an overview of the repository structure and research

## Research Overview

The research examines several key aspects of AI coding tools:

1. **Demographic variations** in AI tool adoption and usage
2. **Professional role differences** in usage patterns and concerns
3. **Experience level influence** on trust and perceptions
4. **Impact on productivity and code quality** across different user groups
5. **Effect on creativity and innovation** in software development
6. **K-means clustering analysis of open-ended responses** to identify patterns in:
   - Desired improvements for AI coding tools
   - Additional comments about AI coding experiences
   - Autonomous software requests (desired future applications)
7. **Desired future capabilities** in AI coding tools

## Key Findings

- ChatGPT is the most widely used AI coding tool (56.7%), followed by GitHub Copilot (36.1%)
- Trust in AI-generated code strongly correlates with reported productivity improvements
- Experienced developers show polarized views on AI tools, while mid-career professionals show consistent moderate trust
- Professional roles significantly predict both usage patterns and concerns about AI tools
- The majority of users report that AI enhances creativity rather than diminishes it
- K-means clustering revealed role-specific priorities and concerns:
  - Students prioritize explanation-focused improvements and learning tools
  - Researchers focus on academic writing support and research platforms
  - Data scientists request advanced features and analytics capabilities
  - Freelancers emphasize security features and project management systems
  - Software developers show bimodal distribution between traditional support and enhanced contextual features
- Trust levels strongly influence the narrative frames participants use when discussing AI tools
- The most requested autonomous software capabilities are learning tools (28.9%) and research platforms (10.3%)

## How to Use This Repository

1. Review the LaTeX research paper (`research_paper.tex`) for a comprehensive, professionally formatted analysis of findings
2. Explore visualizations in the `/final_research` or `/analysis/plots` directories
3. To reproduce the statistical analysis, run the Python script in `/analysis/data_analysis.py`
4. To reproduce the K-means clustering analysis, run the Python script in `/analysis/kmeans_clustering.py`
5. Examine the raw survey data in `/Dataset/dataset.csv`
6. To generate the PDF version of the research paper:
   - On Windows: Run `build_paper.bat`
   - On Unix/Linux/Mac: Run `chmod +x build_paper.sh && ./build_paper.sh`

## Requirements

### To run the analysis scripts:
- Python 3.x
- pandas
- matplotlib
- seaborn
- numpy
- scikit-learn (for K-means clustering)
- nltk (for text preprocessing)
- wordcloud (for generating word clouds)

You can install the required packages with:
```
pip install pandas matplotlib seaborn numpy scikit-learn nltk wordcloud
```

### For NLTK resources:
```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

### To compile the LaTeX document:
- LaTeX distribution (e.g., TeX Live, MiKTeX)
- IEEE conference class files
- Required packages: graphicx, amsmath, amssymb, hyperref, booktabs, multirow, color, float, caption, subcaption, enumerate, listings

You can compile the LaTeX document manually with:
```
pdflatex research_paper.tex
pdflatex research_paper.tex  # Run twice for proper references
```

Or use the provided build scripts for convenience. 