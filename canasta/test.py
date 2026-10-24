from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from consulta import *

chrome_options=Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--disable-web-security')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--disable-extension')
chrome_options.add_argument('--no-proxy-server')

driver = webdriver.Chrome()
MAX = 30
driver.get("https://www.jumbo.cl")

input("ingreasa:")