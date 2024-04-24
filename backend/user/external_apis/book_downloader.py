#!/usr/bin/env python3
"""Used to download books""" 

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from urllib.parse import urljoin
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time

# Global variables
base_url = "https://www.pdfdrive.com/"

def first_page_parsing_and_searching(title):
    # URL of the webpage
    url = base_url + "#"
    
    # Send a GET request to the webpage
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find the div with id 'form-container'
    div = soup.find(id='form-container')
    
    # Find the form with id 'search-form' within the div
    second_form = div.find('form', id='search-form')
    
    # Find the input element within the second form
    input_field = second_form.find("input", id='q')
    
    # Set the value of the input field to "lightning thief"
    input_field["value"] = title
    
    # Get the action attribute of the form
    action = second_form.get('action')
    
    # Construct the complete URL by joining the base URL and the form action
    complete_url = urljoin(url, action)
    
    # Submit the second form by sending a GET request with the input field value as a parameter
    response = requests.get(complete_url, params={input_field['name']: input_field['value']})
    
    # Check if the request was successful
    if response.status_code == 200:
        print("Page one successful.")
        return response
    else:
        print("Page one failed.")
        return None

def second_page(response):
    if not response:
        return None
    # Make a GET request to the response URL
    link = base_url
    
    # Check if the request was successful
    if response.status_code == 200:
        # Print the HTML content of the response
        # Parse the HTML content of the response
        soup = BeautifulSoup(response.content, "html.parser")
        # Find the first div with class 'file-right'
        div = soup.find('div', class_='file-right')
        # Find the 'a' element within the div
        a_tag = div.find('a')
        # Get the href attribute of the 'a' element
        link += a_tag.get('href')
    else:
        print("Failed to retrieve the webpage.")
        
    # Make a GET request to the link
    response = requests.get(link)
    # Check if the request was successful
    progress_link = ""
    
    if response.status_code == 200:
        # Parse the HTML content of the response
        soup = BeautifulSoup(response.content, "html.parser")
        # Find the span with class 'download-button'
        span = soup.find('span', id='download-button')
        # Find the 'a' element within the span
        a_tag = span.find('a')
        # Get the href attribute of the 'a' element
        progress_link = base_url + a_tag.get('href')
        # Print the download link
        print("Page two successful")
        return progress_link
    else:
        print("Failed to retrieve the download page.")
    

def third_page(progress_link):
    if not progress_link:
        return None
    # Setup webdriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    webdriver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=webdriver_service, options=options)
    download_link = ""
    # Open the download link
    driver.get(progress_link)
    # Keep track of the progress bar
    while True:
        try:
            # Find the progress bar
            progress_bar = driver.find_element(By.CSS_SELECTOR, "div[role='progressbar']")
            # Get the aria-valuenow attribute, which represents the current progress
            progress = progress_bar.get_attribute('aria-valuenow')
            # Check if the progress is 100g or more
            if int(progress) >= 100:
                print("Download completed.")
                # Find the 'a' tag with class names 'btn', 'btn-user', 'btn-primary'
                a_tag = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-user.btn-primary")
                # Get the href attribute of the 'a' element
                href = a_tag.get_attribute('href')
                # Append the href to the download_link
                download_link += href
                # Print the download link
                print("Download Link:", download_link)
                break
            else:
                print(f"Download: {progress}% complete.")
        except Exception as e:
            print("Error:", str(e))
            # Sleep for a while before checking again
            time.sleep(1)
    # Close the webdriver
    driver.quit()
    return download_link

def get_dowload_url(title: str):
    """C"""
    first_page_response = first_page_parsing_and_searching(title)
    if not first_page_response:
        raise ValueError("Failed to parse the first page.")
    second_page_response = second_page(first_page_response)
    download_link = third_page(second_page_response)
    

if __name__ == '__main__':
    print(get_dowload_url("harry pottter and the deathly hallows"))

