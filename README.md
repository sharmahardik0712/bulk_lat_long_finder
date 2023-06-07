# Google Map Scraper

This script is a Python program that scrapes business data from Google Maps. It uses Selenium to automate web browsing and extract information such as company names, ratings, reviews counts, addresses, categories, phone numbers, websites, and URLs.

## Prerequisites

Before running the script, ensure that you have the following dependencies installed:

- Python 3.x
- Selenium
- ChromeDriver

You can install Selenium and ChromeDriver using pip:

```shell
pip install selenium
pip install webdriver_manager
```

## Usage

1. Clone the repository or download the script `google_map_scraper.py` to your local machine.

2. Open the script in a text editor of your choice.

3. Update the `urls` variable with the desired cities and their corresponding Google Maps URLs. For example:

   ```python
   urls = [
       ["Pune", "https://www.google.com/maps/search/business+parks+in+pune/..."],
       ["Mumbai", "https://www.google.com/maps/search/business+parks+in+Mumbai/..."],
       # Add more cities and URLs as needed
   ]
   ```

4. Run the script using Python:

   ```shell
   python google_map_scraper.py
   ```

   The script will start scraping the business data from each specified URL and save it to a CSV file named `google_map_business_data.csv`.

## Configuration

The `GoogleMapScraper` class provides some configuration options that you can modify according to your needs:

- `output_file_name`: The name of the output CSV file where the scraped data will be saved.
- `headless`: Set it to `True` if you want to run the Chrome browser in headless mode (without GUI), or `False` otherwise.

## License

This project is licensed under the MIT License. Feel free to modify and use the code according to your needs.

## Disclaimer

This script is intended for educational purposes only. Use it responsibly and make sure to comply with Google's Terms of Service and any applicable laws and regulations in your jurisdiction.
