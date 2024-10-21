
# Amazon Review Sentiment Analysis System

## Goal of the Project

The goal of this application is to provide users with an easy-to-use web interface for analyzing the sentiment of Amazon product reviews. By leveraging VADER Sentiment Analysis and Google Sheets for data retrieval, users can gain insights into customer opinions and sentiment trends in a visual format.


## Features

- **Sentiment Analysis:** Classifies reviews as positive, negative, or neutral using VADER.
- **Data Retrieval:** Fetches review data directly from Google Sheets.
- **Interactive Visualization:** Displays sentiment distribution through pie charts and histograms.
- **User-Friendly Interface:** Easy navigation through a sidebar menu for different functionalities.

## Requirements

To run this project, you need to have the following installed:

- Streamlit
- Pandas
- Plotly
- Google API Client
- VADER Sentiment Analyzer
- Google Auth library

You can install the required packages using:

```bash
pip install streamlit pandas plotly google-auth google-auth-oauthlib google-api-python-client vaderSentiment
```

## Google Sheets API Setup

To set up the Google Sheets API, follow these steps:

1. Go to the [Google Cloud Console](https://console.developers.google.com/).
2. Create a new project.
3. Enable the Google Sheets API for your project.
4. Create credentials for the OAuth 2.0 Client ID.
5. Download the credentials JSON file and rename it to `Key.json`.
6. Place it in the root directory of the project.

## Project Structure

```
.
├── src
│   └── app.py               # Streamlit application code
├── README.md                # Documentation
└── Key.json                 # Google Sheets API credentials
```

## How to Run

Follow these steps to run the application:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/amazon-review-sentiment-analysis.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd amazon-review-sentiment-analysis
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit application:**
   ```bash
   streamlit run src/app.py
   ```

5. **Open your web browser:**  
   After running the command, a local URL will be displayed in the terminal (usually `http://localhost:8501`). Open this link in your web browser.

## Usage Instructions

1. **Home Section:**
   - Displays the title and an introductory image of the system.
   - ![Screenshot 2024-10-21 211108](https://github.com/user-attachments/assets/3017c542-760e-42cd-be97-681381cbd352)


2. **Analyze Sentiment Section:**
   - **Input Fields:** Enter the Google Sheet URL, range (e.g., `Sheet1!A1:A10`), and the column name that contains the reviews.
   - **Analyze Button:** Click to retrieve and analyze the sentiment of the reviews.
   - The results will be displayed in a table, and the analyzed data will be saved as `Review.csv`.
   - ![Screenshot 2024-10-21 211047](https://github.com/user-attachments/assets/f34c3936-a83d-405e-a362-bc10d3f6ef4f)

   - ![Screenshot 2024-10-21 211807](https://github.com/user-attachments/assets/97c04a61-5d8d-4b8d-bedf-187f2bc75ff6)


3. **Visualize the Result Section:**
   - Choose between a Pie chart or a Histogram for visualization.
   - **Pie Chart:** Displays the percentage of positive, negative, and neutral sentiments.
   - **Histogram:** Allows you to select any categorical column for a detailed view of sentiment distribution.
   - ![Screenshot 2024-10-21 211840](https://github.com/user-attachments/assets/2f3dbe55-3eaa-4f45-ac25-8fee94fd72b7)


## Example Dataset Format

The input dataset should be structured in Google Sheets as follows:

| Review Text                               |
|-------------------------------------------|
| "This product is fantastic!"              |
| "Worst purchase I've ever made."          |
| "It's okay, not the best but works fine." |

## Important Notes

- Ensure that the Google Sheet URL and range are correct to retrieve the data successfully.
- The sentiment analysis is based on the VADER sentiment analysis tool, which is suitable for social media texts and reviews.
- The results are saved in a CSV file named `Review3.csv` in the project directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues, pull requests, or suggestions for improving the system. Contributions are welcome!

