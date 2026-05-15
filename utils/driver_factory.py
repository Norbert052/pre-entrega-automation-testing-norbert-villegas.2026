from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os


def get_driver():
    driver_manager = ChromeDriverManager()
    driver_path = driver_manager.install()
    
    # webdriver-manager sometimes returns a path to a non-executable file
    # Find the actual chromedriver.exe in the same directory
    driver_dir = os.path.dirname(driver_path)
    exe_file = os.path.join(driver_dir, "chromedriver.exe")
    
    if not os.path.exists(exe_file):
        exe_file = driver_path
    
    service = Service(exe_file)
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=service, options=options)
    return driver
