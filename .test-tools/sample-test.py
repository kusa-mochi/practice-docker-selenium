from selenium import webdriver
import chromedriver_binary
import time
# import os
# import json

# BROWSER_NAME = os.environ['BROWSER_NAME']
# HOST_NAME = os.environ['HUB_HOST']
# BROWSER_NAME = "chrome"

# BROWSER_FILE_PATH = "_screenshot/" + BROWSER_NAME + "/"
# CURRENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))

# if not os.path.exists(os.path.join(CURRENT_DIR_PATH, BROWSER_FILE_PATH)):
#     os.makedirs(os.path.join(CURRENT_DIR_PATH, BROWSER_FILE_PATH))

# if BROWSER_NAME == "chrome":
#     options = webdriver.ChromeOptions()
# elif BROWSER_NAME == "firefox":
#     options = webdriver.FirefoxOptions()
# else:
#     options = webdriver.EdgeOptions()
#     options.use_chromium = True
# print(BROWSER_NAME)

# options.add_argument('--headless')
# options.add_argument('--window-size=1600,900')

# with webdriver.Remote(
#     command_executor=f'http://localhost:4444/wd/hub',
#     # desired_capabilities=options.to_capabilities(),
#     options=options,
# ) as driver:
#     driver.get('https://www.ecomott.co.jp/')
#     print(driver.current_url)
#     driver.save_screenshot(os.path.join(CURRENT_DIR_PATH, BROWSER_FILE_PATH + "test.png"))

command_executor = f'http://selenium-hub:4444/wd/hub'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certficate-errors')
print(command_executor)
driver = webdriver.Remote(
    command_executor=command_executor,
    options=options
)
driver.maximize_window()
time.sleep(10)
driver.get("https://www.ecomott.co.jp/")
print(driver.current_url)
# driver.save_screenshot(os.path.join)
time.sleep(10)
driver.close()
driver.quit()
print('test completed!')
