# CS50 Web Scraper Project with Enhanced GUI

#### Video Demo: <YOUR_VIDEO_URL_HERE>

#### Description:
This project is a web scraper implemented in Python that extracts quotes from [quotes.toscrape.com](http://quotes.toscrape.com/). The application supports the following features:
- **Web Scraping:** Scrapes multiple pages (user‑configurable) of quotes, extracting each quote's text and author.
- **Data Persistence:** Saves the scraped quotes in a JSON file. If the file already exists, new quotes are merged with the existing data.
- **Random Quote Feature:** Provides the ability to display a random quote from the saved JSON file.
- **Command-Line Interface (CLI):** Users can run the program with various flags to scrape data, display a random quote, or both.
- **Graphical User Interface (GUI):** A modern tkinter-based GUI offers a user-friendly way to control the scraper—allowing users to set the number of pages, specify the output file, and choose whether to scrape quotes or display a random quote.

The project is organized with a `main` function and several helper functions (such as `fetch_html`, `parse_quotes`, `create_quotes_list`, `save_quotes`, and `get_random_quote`) that handle the scraping and file operations. The GUI is built using tkinter with an enhanced layout and styling for a better user experience.

#### Files:
- **project.py**  
  Contains the main entry point and all custom functions, including both CLI and GUI interfaces.
  
- **test_project.py**  
  Contains pytest-based tests for the core functions (fetching, parsing, scraping, saving, and random quote retrieval).

- **requirements.txt**  
  Lists the pip-installable libraries required by the project (e.g., `requests` and `beautifulsoup4`).

#### Features:
- **Web Scraping with Pagination:** Users can scrape one or more pages by specifying the number of pages with the `--pages` argument.
- **File Merging:** If the output JSON file already exists, the scraper merges new quotes with the existing data rather than overwriting it.
- **Random Quote Retrieval:** The program can display a random quote from the JSON file using the `--random` flag.
- **Enhanced GUI:** The GUI (launched with `--gui`) uses tkinter’s ttk module with a modern look (custom fonts, padding, and a scrollable, read-only text widget).

#### How to Run:
1. **Install Dependencies:**  
   Ensure you have Python installed. Install required libraries by running:
   ```bash
   pip install -r requirements.txt
