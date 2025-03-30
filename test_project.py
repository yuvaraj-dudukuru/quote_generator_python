import os
import json
import pytest
from project import fetch_html, parse_quotes, create_quotes_list, save_quotes, get_random_quote

def test_fetch_html():
    url = "http://quotes.toscrape.com/"
    html = fetch_html(url)
    assert isinstance(html, str)
    assert len(html) > 0

def test_parse_quotes():
    sample_html = """
    <div class="quote">
        <span class="text">“Test quote”</span>
        <small class="author">Test Author</small>
    </div>
    """
    quotes = parse_quotes(sample_html)
    assert isinstance(quotes, list)
    assert len(quotes) == 1
    assert quotes[0]["text"] == "“Test quote”"
    assert quotes[0]["author"] == "Test Author"

def test_create_quotes_list(monkeypatch):
    sample_html = """
    <div class="quote">
        <span class="text">“Sample quote”</span>
        <small class="author">Sample Author</small>
    </div>
    """
    def fake_fetch_html(url: str) -> str:
        return sample_html
    monkeypatch.setattr("project.fetch_html", fake_fetch_html)
    quotes = create_quotes_list(3)
    assert len(quotes) == 3
    for quote in quotes:
        assert quote["text"] == "“Sample quote”"
        assert quote["author"] == "Sample Author"

def test_save_quotes(tmp_path):
    quotes = [
        {"text": "Quote 1", "author": "Author 1"},
        {"text": "Quote 2", "author": "Author 2"}
    ]
    file_path = tmp_path / "test_quotes.json"
    save_quotes(quotes, str(file_path))
    assert os.path.exists(file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data == quotes

def test_get_random_quote(tmp_path):
    quotes = [
        {"text": "Random Quote 1", "author": "Author 1"},
        {"text": "Random Quote 2", "author": "Author 2"},
        {"text": "Random Quote 3", "author": "Author 3"}
    ]
    file_path = tmp_path / "quotes.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(quotes, f, ensure_ascii=False, indent=4)
    random_quote = get_random_quote(str(file_path))
    assert random_quote in quotes
