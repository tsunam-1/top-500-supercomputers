from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
data = {}

time.sleep(2)
for year in range (1993, 2026):
    driver.get(f"https://www.top500.org/lists/top500/{year}/06")
    try:
        power = float(driver.find_element(By.XPATH, value="/html/body/div[2]/div/div[1]/table/tbody/tr[1]/td[6]").text.replace(",", ""))
        data[year] = power
    except ValueError:
        pass
with open("power_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Year", "Power (kW)"])
    for year, power in data.items():
        writer.writerow([year, power])