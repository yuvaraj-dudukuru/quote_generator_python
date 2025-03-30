import argparse
import requests
from bs4 import BeautifulSoup
import json
import random
import sys
import os

# --- Helper Functions for Web Scraping ---

def fetch_html(url: str) -> str:
    """
    Fetch HTML content from the given URL.
    Raises requests.HTTPError if the request fails.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_quotes(html: str) -> list:
    """
    Parse HTML content and extract quotes.
    Each quote is a dict with keys "text" and "author".
    """
    soup = BeautifulSoup(html, "html.parser")
    quotes = []
    for quote_div in soup.find_all("div", class_="quote"):
        text = quote_div.find("span", class_="text").get_text()
        author = quote_div.find("small", class_="author").get_text()
        quotes.append({"text": text, "author": author})
    return quotes

def create_quotes_list(pages: int = 1) -> list:
    """
    Scrape the website for the specified number of pages.
    Returns a list of quotes. If a page fails or no quotes are found,
    scraping stops early.
    """
    base_url = "http://quotes.toscrape.com"
    all_quotes = []
    for page in range(1, pages + 1):
        url = base_url + "/" if page == 1 else f"{base_url}/page/{page}/"
        try:
            html = fetch_html(url)
        except requests.HTTPError as e:
            print(f"Warning: Failed to fetch page {page}: {e}")
            break
        quotes = parse_quotes(html)
        if not quotes:
            break
        all_quotes.extend(quotes)
    return all_quotes

def save_quotes(quotes: list, filename: str) -> None:
    """
    Save the list of quotes to a JSON file.
    If the file already exists, load its contents (a list), extend it with new quotes,
    and then write the combined list back.
    """
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                # Try to load existing quotes
                existing = json.load(file)
            # Ensure the data is a list; otherwise, reset it.
            if not isinstance(existing, list):
                existing = []
        except (json.JSONDecodeError, ValueError):
            # If the file content is not valid JSON, start with an empty list.
            existing = []
    else:
        existing = []

    # Combine existing quotes with the new ones.
    combined = existing + quotes

    # Write the combined list to the file (overwriting previous content).
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(combined, file, ensure_ascii=False, indent=4)

def get_random_quote(filename: str) -> dict:
    """
    Load quotes from the given JSON file and return one random quote.
    """
    with open(filename, "r", encoding="utf-8") as f:
        quotes = json.load(f)
    if not quotes:
        return {}
    return random.choice(quotes)

# --- GUI Code Using tkinter ---

def run_gui():
    try:
        import tkinter as tk
        from tkinter import ttk, messagebox
    except ImportError:
        sys.exit("tkinter is required for the GUI")
    
    # Create main window
    root = tk.Tk()
    root.title("CS50 Web Scraper Enhanced GUI")
    root.geometry("500x400")
    root.configure(bg="#ececec")  # light grey background

    # Set up ttk styling for a modern look
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("TLabel", background="#ececec", font=("Helvetica", 12))
    style.configure("TButton", font=("Helvetica", 12, "bold"))
    style.configure("TEntry", font=("Helvetica", 12))

    # Header label
    header = ttk.Label(root, text="CS50 Web Scraper", font=("Helvetica", 20, "bold"), foreground="#333333")
    header.grid(row=0, column=0, columnspan=2, pady=20)

    # Number of pages label and entry
    ttk.Label(root, text="Number of pages:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    pages_var = tk.StringVar(value="1")
    pages_entry = ttk.Entry(root, textvariable=pages_var, width=10)
    pages_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    # Output filename label and entry
    ttk.Label(root, text="Output file:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    outfile_var = tk.StringVar(value="quotes.json")
    outfile_entry = ttk.Entry(root, textvariable=outfile_var, width=20)
    outfile_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    # Define actions before creating buttons
    def scrape_action():
        try:
            pages = int(pages_var.get())
        except ValueError:
            messagebox.showerror("Error", "Number of pages must be an integer.")
            return
        outfile = outfile_var.get().strip()
        quotes = create_quotes_list(pages)
        save_quotes(quotes, outfile)
        result_text.config(state="normal")
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"Scraped and saved {len(quotes)} quotes to {outfile}")
        result_text.config(state="disabled")

    def random_action():
        outfile = outfile_var.get().strip()
        try:
            quote = get_random_quote(outfile)
        except FileNotFoundError:
            messagebox.showerror("Error", f"File {outfile} not found. Please scrape first.")
            return
        result_text.config(state="normal")
        result_text.delete("1.0", tk.END)
        if quote:
            result_text.insert(tk.END, f'"{quote["text"]}"\n— {quote["author"]}')
        else:
            result_text.insert(tk.END, "No quotes found in the file.")
        result_text.config(state="disabled")

    # Frame for buttons with padding
    btn_frame = ttk.Frame(root)
    btn_frame.grid(row=3, column=0, columnspan=2, pady=15)
    scrape_btn = ttk.Button(btn_frame, text="Scrape Quotes", command=scrape_action)
    scrape_btn.grid(row=0, column=0, padx=10)
    random_btn = ttk.Button(btn_frame, text="Show Random Quote", command=random_action)
    random_btn.grid(row=0, column=1, padx=10)

    # Result area: Text widget with vertical scrollbar
    result_frame = ttk.Frame(root)
    result_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    # Allow the result frame to expand
    root.grid_rowconfigure(4, weight=1)
    root.grid_columnconfigure(0, weight=1)
    result_text = tk.Text(result_frame, height=10, width=50, wrap="word", font=("Helvetica", 12))
    result_text.pack(side="left", fill="both", expand=True)
    scrollbar = ttk.Scrollbar(result_frame, orient="vertical", command=result_text.yview)
    scrollbar.pack(side="right", fill="y")
    result_text.config(yscrollcommand=scrollbar.set)
    result_text.config(state="disabled")

    root.mainloop()


# --- Command-Line Interface (CLI) ---

def main():
    parser = argparse.ArgumentParser(
        description="Scrape quotes.toscrape.com and optionally display a random quote."
    )
    parser.add_argument(
        "--pages", type=int, default=1,
        help="Number of pages to scrape (default: 1)"
    )
    parser.add_argument(
        "--outfile", type=str, default="quotes.json",
        help="Output JSON file (default: quotes.json)"
    )
    parser.add_argument(
        "--random", action="store_true",
        help="If provided, print a random quote from the JSON file instead of scraping"
    )
    parser.add_argument(
        "--gui", action="store_true",
        help="Launch a GUI for the application"
    )
    args = parser.parse_args()

    if args.gui:
        run_gui()
    elif args.random:
        try:
            quote = get_random_quote(args.outfile)
        except FileNotFoundError:
            print(f"File {args.outfile} not found. Run the scraper first.")
            return
        if quote:
            print(f'"{quote["text"]}" — {quote["author"]}')
        else:
            print("No quotes found in the file.")
    else:
        quotes = create_quotes_list(args.pages)
        save_quotes(quotes, args.outfile)
        print(f"Scraped and saved {len(quotes)} quotes to {args.outfile}")

if __name__ == "__main__":
    main()
