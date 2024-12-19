from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl

# Path where the WebDriver is located
EXECUTABLE_PATH = "/home/mohamed/workspaces/workspace-advancedpython/Test Selenium/chromedriver"

# Search Term
SEARCH_TERM = "hello world"

# Initialize the Selenium WebDriver
service = Service(executable_path=EXECUTABLE_PATH)
driver = webdriver.Chrome(service=service)

try:
    # Open Google
    driver.get("https://google.com")

    # Wait for the search bar to be present
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
    )

    # Locate the search input element
    input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
    input_element.clear()
    input_element.send_keys(SEARCH_TERM + Keys.ENTER)

    # Wait for the results to load
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "N54PNb"))
    )

    # Locate the search result containers
    results = driver.find_elements(By.CLASS_NAME, "N54PNb")

    # Extract the first 10 results
    search_results = []
    for result in results[:10]:
        try:
            # Locate the element containing the title, URL, and description
            element = result.find_element(
                By.CSS_SELECTOR, "a[jsname='UWckNb']")

            # Extract the title
            title_element = element.find_element(
                By.CSS_SELECTOR, "h3.LC20lb.MBeuO.DKV0Md")
            title = title_element.text

            # Extract the URL
            url = element.get_attribute("href")

            # Extract the description
            description_element = result.find_element(
                By.CSS_SELECTOR,
                "div.VwiC3b.yXK7lf.p4wth.r025kc.hJNv6b.Hdw6tb")
            description = description_element.text

            search_results.append({
                "Title": title,
                "Description": description,
                "URL": url,
            })
        except Exception as e:
            print(f"Error extracting result: {e}")

    # Save results to an Excel file
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Search Results"

    # Add headers
    sheet.append(["Title", "Description", "URL"])

    # Add data rows
    for result in search_results:
        sheet.append([result['Title'], result['Description'], result['URL']])

    # Save the workbook
    try:
        workbook.save("search_results.xlsx")
    except Exception as e:
        print(f"Error saving results to Excel: {e}")


finally:
    # Close the browser
    driver.quit()
