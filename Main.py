from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import sleep

import os

# Makes sure the program is running in the correct directory.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def watch_video_via_proxy(website_domain, proxy_count):
    # Set up Firefox options
    firefox_options = Options()
    firefox_options.set_preference("general.useragent.override", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36')
    firefox_options.set_preference("intl.accept_languages", "en-US")
    firefox_options.set_preference('permissions.default.stylesheet', 2)
    firefox_options.set_preference('permissions.default.image', 2)

    # Create a new instance of the Firefox driver
    GeckoDriverManager().install()
    driver = webdriver.Firefox(options=firefox_options)


    driver.get('https://www.blockaway.net/')
    sleep(2)  # Wait for 2 seconds

    text_box = driver.find_element(By.ID, 'url')
    text_box.send_keys(f'{website_domain}')
    text_box.send_keys(Keys.RETURN)

    sleep(5)  # Wait for 5 seconds

    for i in range(proxy_count - 1):  # Minus 1 because we have already opened one
        driver.execute_script("window.open('https://www.blockaway.net/')")
        sleep(2)  # Wait for 2 seconds
        driver.switch_to.window(driver.window_handles[-1])
        sleep(2)  # Wait for 2 seconds
        text_box = driver.find_element(By.ID, 'url')
        text_box.send_keys(f'{website_domain}')
        text_box.send_keys(Keys.RETURN)
        sleep(5)  # Wait for 5 seconds

    input("Viewers have all been sent. You can press enter to close it...")

if __name__ == "__main__":
    website_domain = input("Enter the website domain")
    proxy_count = int(input("How many viewers"))

    watch_video_via_proxy(website_domain, proxy_count)
