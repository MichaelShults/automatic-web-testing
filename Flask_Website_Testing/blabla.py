from playwright.sync_api import sync_playwright
import time


keywords = { 
    "cat": False,
    "dog": True

}

def test_flask_search(search_term):
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False)
        page = browser.new_page()

        page.goto("127.0.0.1:8080")

        page.fill("input[name='q']", search_term)
        time.sleep(3)
        page.press("input[name='q']", "Enter")
        time.sleep(3)

        page.wait_for_load_state()
        try:
            assert (page.locator("h3").count() > 0) == keywords[search_term], "incorrect number of results."
        except AssertionError as e:
            print(f"{e}: Test for {search_term} failed.")
        browser.close()

for k in keywords.keys():
    test_flask_search(k)






# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# driver = webdriver.Chrome()
# driver.get("https://www.google.com")

# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys("actualized.org")
# search_box.send_keys(Keys.RETURN)

# time.sleep(3)

# results = driver.find_elements(By.CSS_SELECTOR, "h3")
# assert len(results) > 0, "No search results found"

# print("Test passed!")
# driver.quit()





# import requests


# response = requests.get("https://www.google.com")
# assert response.status_code == 200, "API request failed"
# print("API test passed!")