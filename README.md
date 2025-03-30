# AI Coding Tools Impact Analysis

This repository contains data analysis and research on the impact of AI coding tools on developer productivity and perception. The project analyzes survey data from 97 professionals with diverse backgrounds to understand usage patterns, perceptions, and concerns related to AI coding tools.

## Repository Structure

### `/Dataset`
Contains the raw survey data used for the analysis:
- `dataset.csv` - Survey responses from 97 participants, including demographics, AI tool usage patterns, impacts, and perceptions

### `/analysis`
Contains the code and intermediate outputs from the data analysis process:
- `data_analysis.py` - Python script that performs statistical analysis and generates visualizations
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

### `/final_research`
Contains the final research outputs and presentation materials:
- `research_paper.md` - Complete research paper with findings and discussion
- Analysis results and visualizations for presentation

## Research Overview

The research examines several key aspects of AI coding tools:

1. **Demographic variations** in AI tool adoption and usage
2. **Professional role differences** in usage patterns and concerns
3. **Experience level influence** on trust and perceptions
4. **Impact on productivity and code quality** across different user groups
5. **Effect on creativity and innovation** in software development
6. **Desired future capabilities** in AI coding tools

## Key Findings

- ChatGPT is the most widely used AI coding tool (56.7%), followed by GitHub Copilot (36.1%)
- Trust in AI-generated code strongly correlates with reported productivity improvements
- Experienced developers show polarized views on AI tools, while mid-career professionals show consistent moderate trust
- Professional roles significantly predict both usage patterns and concerns about AI tools
- The majority of users report that AI enhances creativity rather than diminishes it
- The most requested autonomous software capabilities are learning tools (25.8%) and research tools (20.6%)

## How to Use This Repository

1. Review the research paper in `/final_research/research_paper.md` for a comprehensive overview of findings
2. Explore visualizations in the `/final_research` or `/analysis/plots` directories
3. To reproduce the analysis, run the Python script in `/analysis/data_analysis.py`
4. Examine the raw survey data in `/Dataset/dataset.csv`

## Requirements

To run the analysis script, you need:
- Python 3.x
- pandas
- matplotlib
- seaborn
- numpy

You can install the required packages with:
```
pip install pandas matplotlib seaborn numpy
``` 