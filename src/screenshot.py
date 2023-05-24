from selenium import webdriver
from selenium.webdriver.common.by import By
import time



def get_screenshot(text: str, url) -> str | None:
    try:
        # Configure the Selenium WebDriver (e.g., Chrome)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run Chrome in headless mode
        options.add_argument('--no-sandbox')  # Run Chrome in headless mode
        options.add_argument('--encoding=utf-8')  # Set the desired encoding
        driver = webdriver.Chrome(options=options)

        # Load the web page
        driver.get(url)
        time.sleep(30)
        div_element = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div/article/div/div[2]/div/div[2]/div[1]/ul')
        comments = div_element.find_elements(By.CLASS_NAME, "_a9ym")
        for comment in comments:
            comment_section = comment.find_element(By.CSS_SELECTOR, 'div._a9zr > div._a9zs > span')
            comment_text = comment_section.get_attribute("innerHTML")
            if comment_text == text:
                return comment.screenshot_as_base64
    except Exception as e:
        print(f"Error {e}")
        return None