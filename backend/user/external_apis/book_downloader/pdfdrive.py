#!/usr/bin/env python3
"""
Used to download books from PDF Drive.
"""

import time
import asyncio
import logging
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# Global variables
BASE_URL = "https://www.pdfdrive.com/"

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def first_page_parsing_and_searching(title: str) -> requests.Response:
    """
    Search for the book title on the first page.
    """
    while True:
        try:
            url = BASE_URL + "#"
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")
            div = soup.find(id='form-container')
            search_form = div.find('form', id='search-form')
            input_field = search_form.find("input", id='q')
            input_field["value"] = title
            action = search_form.get('action')
            complete_url = urljoin(url, action)

            response = requests.get(complete_url, params={input_field['name']: input_field['value']}, timeout=10)
            response.raise_for_status()

            logging.info("Page one successful.")
            return response
        except Exception as err:
            logging.error("Error: %s", err)
            logging.info("Failed to retrieve the first webpage...retrying after 10 seconds")
            time.sleep(10)


def second_page(response: requests.Response) -> str:
    """
    Select the book on the second page.
    """
    while True:
        try:
            if not response:
                return ""
            link = BASE_URL

            soup = BeautifulSoup(response.content, "html.parser")
            div = soup.find('div', class_='file-right')
            a_tag = div.find('a')
            link += a_tag.get('href')

            response = requests.get(link, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")
            span = soup.find('span', id='download-button')
            a_tag = span.find('a')
            progress_link = BASE_URL + a_tag.get('href')

            logging.info("Page two successful.")
            return progress_link
        except Exception as err:
            logging.error("Error: %s", err)
            logging.info("Failed to retrieve the second webpage...retrying after 10 seconds")
            time.sleep(10)


def third_page(progress_link: str) -> str:
    """
    Get the download book link on the third page.
    """
    if not progress_link:
        return ""

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    webdriver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=webdriver_service, options=options)
    download_link = ""

    driver.get(progress_link)
    
    progress_bar_selectors = [
    "div[role='progressbar']",
    # Add more CSS selectors for additional progress bars if needed
    ]
    
    a_tag_selectors = [
        "a.btn.btn-success.btn-responsive",
        "a.btn.btn-primary.btn-user"
        # Add more CSS selectors for additional a_tag selectors if needed       
    ]

    while True:
        try:
            progress = None
            for selector in progress_bar_selectors:
                try:
                    progress_bar = driver.find_element(By.CSS_SELECTOR, selector)
                    progress = progress_bar.get_attribute('aria-valuenow')
                    break  # Exit the loop if a progress bar is found
                except NoSuchElementException:
                    continue 

            if int(progress) >= 100:
                logging.info("Download completed.")
                for selector in a_tag_selectors:
                    try:
                        a_tag = driver.find_element(By.CSS_SELECTOR, selector)
                        break  # Exit the loop if a progress bar is found
                    except NoSuchElementException:
                        continue 
                download_link = a_tag.get_attribute('href')
                logging.info("Download Link: %s", download_link)
                break
        except Exception as err:
            logging.error("Error: %s", err)
            break

    driver.quit()
    return download_link


def get_download_url(title: str) -> str:
    """
    Main function of the script to get the download URL for a book title.
    """
    first_page_response = first_page_parsing_and_searching(title)
    if not first_page_response:
        raise ValueError("Failed to parse the first page.")
    second_page_response = second_page(first_page_response)
    if not second_page_response:
        raise ValueError("Failed to parse the second page.")
    download_link = third_page(second_page_response)
    return download_link


async def process_query(query: str, file):
    """
    Process each query asynchronously and write the download link to a file.
    """
    query = query.strip()
    try:
        download_link = await asyncio.get_event_loop().run_in_executor(None, get_download_url, query)
        if download_link:
            file.write(download_link + '\n')
        else:
            logging.warning("No download link found for query: %s", query)
    except Exception as err:
        logging.error("Error processing query '%s': %s", query, err)


if __name__ == '__main__':
    queries = []
    with open('example_booklist.txt', 'r') as file:
        queries = file.readlines()

    with open('download_links.txt', 'w') as file:
        loop = asyncio.get_event_loop()
        tasks = [process_query(query, file) for query in queries]
        loop.run_until_complete(asyncio.gather(*tasks))
        loop.close()
