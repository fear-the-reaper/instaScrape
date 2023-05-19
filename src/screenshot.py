from selenium import webdriver
from selenium.webdriver.common.by import By
import time



def get_screenshot(text: str, url) -> str | None:
    # Configure the Selenium WebDriver (e.g., Chrome)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=options)

    # Load the web page
    driver.get(url)
    time.sleep(30)
    div_element = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div/article/div/div[2]/div/div[2]/div[1]/ul')
    comments = div_element.find_elements(By.CLASS_NAME, "_a9ym")
    for comment in comments:
        comment_section = comment.find_element(By.CSS_SELECTOR, 'div._a9zr > div._a9zs > span')
        comment_text = comment_section.text
        if comment_text == text:
            file_name = f"{comment_text}.png"
            comment.screenshot(file_name)
            return file_name
        
    return None