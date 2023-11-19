from selenium import webdriver
import chromedriver_binary
import time
import os

BROWSER_NAME = os.environ['BROWSER_NAME']

BROWSER_FILE_PATH = "_screenshot/" + BROWSER_NAME + "/"
CURRENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists(os.path.join(CURRENT_DIR_PATH, BROWSER_FILE_PATH)):
    os.makedirs(os.path.join(CURRENT_DIR_PATH, BROWSER_FILE_PATH))

# options.add_argument('--window-size=1600,900')

command_executor = f'http://selenium-hub:4444/wd/hub'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certficate-errors')
print(command_executor)
with webdriver.Remote(
    command_executor=command_executor,
    options=options,
) as driver:
    driver.maximize_window()
    time.sleep(5)
    driver.get("https://slash-mochi.net/")
    print(driver.current_url)
    driver.save_screenshot(os.path.join(CURRENT_DIR_PATH, BROWSER_FILE_PATH, "test.png"))
    time.sleep(10)
    print('test completed!')
