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
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# Global variables
BASE_URL = "https://www.pdfdrive.com/"

# Configure logging
logging.basicConfig(
                    filename="pdfdrive.log",
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s'
                    )

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

            response = requests.get(
                                    complete_url,
                                    params={input_field['name']: input_field['value']},
                                    timeout=10
                                    )

            response.raise_for_status()

            logging.info("Page one successful.")
            return response
        except requests.exceptions.HTTPError as err:
            logging.error("HTTP Error: %s", err)
            logging.info("Failed to retrieve the first webpage...retrying after 10 seconds")
            time.sleep(10)
        except NoSuchElementException as err:
            logging.error("Element not found: %s", err)

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

            response = requests.get(link, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")
            span = soup.find('span', id='download-button')
            a_tag = span.find('a')
            progress_link = BASE_URL + a_tag.get('href')

            logging.info("Page two successful.")
            return progress_link
        except requests.exceptions.HTTPError as err:
            logging.error("Error: %s", err)
            logging.info("Failed to retrieve the second webpage...retrying after 10 seconds")
            time.sleep(10)
        except NoSuchElementException as err:
            logging.error("Element not found: %s", err)
            break
        except AttributeError as err:
            logging.error("Attribute error: %s", err)
            break


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
        # pylint: disable=W0718
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


async def process_query(query: str, output_file):
    """
    Process a query and write the download link to the output file.
    """
    try:
        download_link = await asyncio.get_event_loop().run_in_executor(
                                                                        None,
                                                                        get_download_url,
                                                                        query
                                                                        )
        if download_link:
            output_file.write(download_link + '\n')
        else:
            logging.warning("No download link found for query: %s", query)
    # pylint: disable=W0718
    except Exception as err:
        logging.error("Error processing query '%s': %s", query, err)


if __name__ == '__main__':
    queries = []
    with open("example_booklist.txt", "r", encoding='utf-8') as file:
        queries = file.readlines()

    with open("download_links.txt", "w", encoding='utf-8') as output_file:
        for query in queries:
            asyncio.run(process_query(query.strip(), output_file))
            time.sleep(10)
