# Amazon-Reviews-Sentimental-Analysis
## Overview 
This application allows users to analyze the sentiment of Amazon product reviews using a web interface built with Streamlit. The system retrieves review data from Google Sheets, processes the text using VADER Sentiment Analysis, and visualizes the results with interactive charts created using Plotly.

## Features
Sentiment Analysis: Classifies reviews as positive, negative, or neutral using VADER.
Data Retrieval: Fetches review data directly from Google Sheets.
Interactive Visualization: Displays sentiment distribution through pie charts and histograms.
User-Friendly Interface: Easy navigation through a sidebar menu for different functionalities.

## Requirements
To run this project, you need to have the following installed:

Python 3.8 or higher
Streamlit
Pandas
Plotly
Google API Client
VADER Sentiment Analyzer
Google Auth library

You can install the required packages using:

bash
Copy code
pip install streamlit pandas plotly google-auth google-auth-oauthlib google-api-python-client vaderSentiment

### Google Sheets API Setup
Go to the Google Cloud Console.
Create a new project.
Enable the Google Sheets API for your project.
Create credentials for the OAuth 2.0 Client ID.
Download the credentials JSON file and rename it to Key.json. Place it in the root directory of the project.

## Project Structure
graphql
Copy code
.
├── src
│   └── app.py               # Streamlit application code
├── README.md                # Documentation
└── Key.json                 # Google Sheets API credentials
## How to Run
### 1.Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/amazon-review-sentiment-analysis.git
### 2.Navigate to the project directory:

bash
Copy code
cd amazon-review-sentiment-analysis
### 3. Install the dependencies:

bash
Copy code
pip install -r requirements.txt
### 4. Run the Streamlit application:

bash
Copy code
streamlit run src/app.py
### 5.Open your web browser:
After running the command, a local URL will be displayed in the terminal (usually http://localhost:8501). Open this link in your web browser.

## Usage Instructions
## 1. Home Section:

Displays the title and an introductory image of the system.
## 2. Analyze Sentiment Section:

Input Fields: Enter the Google Sheet URL, range (e.g., Sheet1!A1:A10), and the column name that contains the reviews.
Analyze Button: Click to retrieve and analyze the sentiment of the reviews.
The results will be displayed in a table, and the analyzed data will be saved as Review3.csv.
## 3. Visualize the Result Section:

Choose between a Pie chart or a Histogram for visualization.
Pie Chart: Displays the percentage of positive, negative, and neutral sentiments.
Histogram: Allows you to select any categorical column for a detailed view of sentiment distribution.

## Example Dataset Format
The input dataset should be structured in Google Sheets as follows:

Review Text
"This product is fantastic!"
"Worst purchase I've ever made."
"It's okay, not the best but works fine."

## Important Notes
Ensure that the Google Sheet URL and range are correct to retrieve the data successfully.
The sentiment analysis is based on the VADER sentiment analysis tool, which is suitable for social media texts and reviews.
The results are saved in a CSV file named Review3.csv in the project directory.
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
Feel free to submit issues, pull requests, or suggestions for improving the system. Contributions are welcome!




