from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

BROWSER_NAME = os.environ['BROWSER_NAME']

BROWSER_FILE_PATH = "_screenshot/" + BROWSER_NAME + "/"
CURRENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists(os.path.join(CURRENT_DIR_PATH, BROWSER_FILE_PATH)):
    os.makedirs(os.path.join(CURRENT_DIR_PATH, BROWSER_FILE_PATH))

command_executor = f'http://selenium-hub:4444/wd/hub'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certficate-errors')
options.add_argument('--window-size=1600,900')
print(command_executor)
with webdriver.Remote(
    command_executor=command_executor,
    options=options,
) as driver:
    action = ActionChains(driver)
    wait = WebDriverWait(driver, 15)

    driver.maximize_window()
    driver.get("https://slash-mochi.net/")
    time.sleep(7)
    driver.save_screenshot(os.path.join(CURRENT_DIR_PATH, BROWSER_FILE_PATH, "home.png"))
    search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#site-navigation span.search-item')))
    search_button.click()
    # action.move_to_element_with_offset(search_button, 5, 5)
    # action.click()
    # action.perform()
    time.sleep(1)
    search_input = driver.find_element(By.CLASS_NAME, 'search-field')
    search_input.send_keys('linux')
    time.sleep(1)
    search_input.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.save_screenshot(os.path.join(CURRENT_DIR_PATH, BROWSER_FILE_PATH, "linux.png"))
    print('test completed!')
