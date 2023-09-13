# Movie Transcript Web Scraping Script

## Overview

This Python script is designed to scrape movie transcripts from a specific website using the BeautifulSoup library for HTML parsing and the Requests library for fetching web pages. In this example, we'll use the movie "Harry Potter and the Prisoner of Azkaban" as an illustration.

## Script Workflow

1. **Import Libraries**: The script starts by importing the necessary libraries, BeautifulSoup and Requests.

2. **Fetching Web Content**: It sends an HTTP request to the specified website (https://subslikescript.com/movie/Harry_Potter_and_the_Prisoner_of_Azkaban-304141) to retrieve the HTML content of the page containing the movie transcript.

3. **HTML Parsing**: BeautifulSoup is used to parse the HTML content, making it easier to navigate and extract specific elements.

4. **Extracting Content**: The script identifies the parent `div` element that encapsulates all the transcript content and extracts the title of the transcript and the transcript text itself.

5. **Writing to File**: The extracted transcript is written to a text file named 'harry-potter.txt'. The title is prepended to the transcript text for identification.

## How to Use

1. Ensure you have Python installed on your system.

2. Install the required libraries using pip:
3. pip install beautifulsoup4 
4. pip install request
5. Copy and paste the provided script into a Python file (e.g., `movie_transcript_scraper.py`).

6. Run the script, and it will fetch and save the transcript of "Harry Potter and the Prisoner of Azkaban" in a text file.

## Benefits

- **Automation**: The script automates the process of scraping movie transcripts from the web, eliminating the need for manual copying and pasting.

- **Data Accessibility**: Extracted transcripts can be easily stored and organized for future reference or analysis.

- **Customization**: You can adapt the script to scrape transcripts from other movie pages or websites by modifying the `website` variable.

## Conclusion

This Python script serves as a simple yet effective tool for extracting movie transcripts from web pages. It demonstrates the use of BeautifulSoup and Requests for web scraping and can be customized to scrape transcripts from various sources, making it valuable for movie enthusiasts and researchers.
"""


