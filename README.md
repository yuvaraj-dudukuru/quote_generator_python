# CS50 QuoteVault

#### Video Demo: https://www.youtube.com/watch?v=YOUR_VIDEO_URL_HERE

#### Description:
CS50 QuoteVault is a Python-based web scraper and graphical application designed to collect inspirational quotes from [quotes.toscrape.com](http://quotes.toscrape.com/). The project features both a command-line interface (CLI) and an enhanced graphical user interface (GUI) built using tkinter. Users can specify how many pages to scrape, choose the output JSON file, and even retrieve a random quote from the saved data.

The application works by:
- **Scraping Quotes:** It connects to the website, retrieves the HTML for each page (with pagination support), and extracts quotes along with their respective authors using BeautifulSoup.
- **Data Persistence:** Instead of overwriting data, the scraper merges new quotes with any previously saved quotes. This ensures that each scraping session builds on a cumulative archive of inspirational quotes.
- **Random Quote Feature:** The project can display a random quote from the stored JSON file, providing an element of surprise and inspiration.
- **Graphical User Interface:** An enhanced GUI allows users to interact with the scraper in a more intuitive manner. The GUI includes modern styling, a clean layout using tkinter's ttk module, and a read-only text widget with a scrollbar for output display.

This project is structured to demonstrate solid software engineering practices: modular code design, thorough documentation, and automated testing using pytest.

#### Project Structure:
- **project.py:**  
  Contains the main entry point and all custom functions. This file includes:
  - Web scraping functions: `fetch_html`, `parse_quotes`, `create_quotes_list`
  - Data persistence: `save_quotes`
  - Random quote retrieval: `get_random_quote`
  - GUI implementation: `run_gui`
  - Command-line interface (CLI) logic via argparse
- **test_project.py:**  
  Contains pytest-based tests for key functions (HTML fetching, quote parsing, data merging, and random quote retrieval) ensuring that each module functions correctly.
- **requirements.txt:**  
  Lists all pip-installable dependencies (e.g., `requests` and `beautifulsoup4`).
- **README.md:**  
  This documentation file.

#### How to Run:

1. **Installation:**
   - Ensure you have Python installed.
   - Install the required dependencies by running:
     ```bash
     pip install -r requirements.txt
     ```

2. **Command-Line Interface (CLI) Usage:**
   - **To scrape quotes:**
     ```bash
     python project.py --pages 3 --outfile quotes.json
     ```
     This command scrapes quotes from 3 pages and saves (or merges into) `quotes.json`.
   - **To display a random quote:**
     ```bash
     python project.py --random --outfile quotes.json
     ```

3. **Graphical User Interface (GUI) Usage:**
   - Launch the GUI by running:
     ```bash
     python project.py --gui
     ```
     In the GUI window, you can enter the number of pages to scrape and the output filename, then click the appropriate buttons to either scrape new quotes or display a random quote from the JSON file.

4. **Running Tests:**
   - Run the tests using pytest from the project’s root directory:
     ```bash
     pytest test_project.py
     ```

#### Design Decisions:
- **Data Merging:**  
  The `save_quotes` function checks if the output file exists. If so, it loads the existing data (expected to be a JSON array) and merges the new quotes with the old ones. This prevents data loss and maintains a cumulative archive.
- **User Interface:**  
  The GUI was enhanced using tkinter’s ttk module for a modern look. A grid layout ensures that elements are well-aligned, and a scrollable read-only text widget provides a clear display for messages and quotes.
- **Modular Code Structure:**  
  All functionality is broken down into specific helper functions (e.g., for fetching HTML, parsing quotes, saving data, etc.) which makes the code easier to maintain, test, and extend.

#### Author Information:
- **Name:** Jane Doe  
- **GitHub Username:** janedoe  
- **edX Username:** janedoe_edX  
- **City and Country:** New York, USA  
- **Date Recorded:** 2025-03-30

#### Future Enhancements:
- **Enhanced Error Handling:**  
  Improve error handling for network failures and unexpected HTML changes on the target website.
- **Additional Data Extraction:**  
  Extend the scraper to collect more details (e.g., tags, author biographies).
- **GUI Improvements:**  
  Add more interactive elements such as progress indicators, better layout responsiveness, and customizable themes.
- **Data Analysis:**  
  Implement features to analyze the collected quotes (e.g., frequency analysis of authors or topics).

---
