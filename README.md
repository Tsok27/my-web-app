# Vehicle Market Analysis Dashboard

## Project Description
An interactive web application for analyzing used vehicle market trends, featuring:
- Price distribution visualizations
- Exploratory data analysis tools

## Technologies Used
- **Python 3.9+**
- **Streamlit** - Web application framework
- **Pandas** - Data processing and analysis
- **Plotly Express** - Interactive visualizations
- **Git** - Version control

## Installation & Setup

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Step-by-Step Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/vehicle-analysis.git
   cd vehicle-analysis

2. Create and activate a virtual environment:
   python -m venv venv

3. install dependencies:

4. Run the application:

5. Access dashboard in your browser:

## Project Structure
vehicle-analysis/
├── data/                   # Processed dataset
│   └── vehicles_us_cleaned.csv
├── notebooks/              # Jupyter notebooks
│   └── EDA.ipynb
├── app.py                  # Main application
└── README.md               # Project documentation

## Features
- Histograms : Looked at odometer, model_year per example
- Scatter Plots: Price vs. Fuel, Price vs Cylinders for example
- Data Filtering & Data Inspections

## Usage Guide
1. Launch the application using streamlit run app.py
2. Use sidebar to filter data
3. Hover over visualizations for detailed information
4. Toggle the "Show raw data" checkbox to inspect underlying data
