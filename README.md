# Async Web Crawler

This project is an asynchronous web crawler built with Python, using Poetry for dependency management. It scrapes data
from a website, parses it, and saves the results into a CSV file.

## Features

- **Asynchronous**: Utilizes `asyncio` and `httpx` for efficient, parallel page scraping.
- **Configuration**: Settings are managed through a `.env` file using `pydantic-settings`.
- **HTML Parsing**: Uses `BeautifulSoup` for robust HTML parsing.
- **Data Saving**: Outputs results into a CSV file.
- **Dependency Management**: Managed with Poetry for streamlined setup and installation.

---

1. **Clone the repository:**
   ```
   git clone https://github.com/your-repository/async-web-crawler.git
   cd async-web-crawler
   
2. **Install Poetry: Poetry is a dependency management tool. Install it by following the official guide.**

3. **Install dependencies**
   ```
   poetry install

4. **Set up the .env file: Create a .env file in the ParsingWebData directory with the following content:**

   ```
   DOMAIN_URL=https://example.com
   NUM_PAGES=10
   OUTPUT_PATH=./output
   CSV_FILE_NAME=data.csv
   ```

**Usage**

1. Run the crawler: Use Poetry to execute the script:
    ```
   poetry run python main.py

This will start the scraping process and save the data to output/data.csv.

2. Output: After the process is complete, the results will be saved in a CSV file in the specified OUTPUT_PATH.

**Dependencies**

Dependencies are managed with Poetry and specified in the pyproject.toml file.

**Key Libraries:**

 *    httpx: For asynchronous HTTP requests.
 *    beautifulsoup4: For HTML parsing.
 *    loguru: For logging.
 *    pydantic and pydantic-settings: For configuration management.
