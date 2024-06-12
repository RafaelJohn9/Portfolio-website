#!/usr/bin/env python3
"""
Used to download books from PDF Drive.
"""
import time
import logging
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
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

            soup = BeautifulSoup(response.content, "html.parser")
            div = soup.find('div', class_='file-right')
            a_tag = div.find('a')
            page_link = BASE_URL + a_tag.get('href')
            page_response = requests.get(page_link, timeout=10)
            soup = BeautifulSoup(page_response.content, "html.parser")
            download_button = soup.find('span', id='download-button')
            a_tag = download_button.find('a')
            progress_link = a_tag.get('href')

            logging.info("Page two successful.")
            return BASE_URL + progress_link

        except requests.exceptions.HTTPError as err:
            logging.error("Error: %s", err)
            logging.info("Failed to retrieve the second webpage...retrying after 5 seconds")
            time.sleep(5)
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

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    webdriver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=webdriver_service, options=options)
    download_link = ""

    driver.get(progress_link)

    progress_bar_selectors = [
        'div.progress-bar.progress-bar-striped.progress-bar-animated',
        "div.progress-bar",
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
            if not progress:
                logging.info("Progress not found.")
                break

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
        return None

    second_page_response = second_page(first_page_response)

    if not second_page_response:
        return None

    download_link = third_page(second_page_response)

    return download_link

if __name__ == '__main__':
    BOOK_TITLE = input("Enter the book title: ")
    book_download_link = get_download_url(BOOK_TITLE)
    if book_download_link:
        print(book_download_link)
    else:
        print("Book not found")
