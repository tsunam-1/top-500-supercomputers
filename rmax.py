from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
data = {}

for year in range (1993, 2026):
    driver.get(f"https://www.top500.org/lists/top500/{year}/06")
    rmax = float(driver.find_element(By.XPATH, value="/html/body/div[2]/div/div[1]/table/tbody/tr[1]/td[4]").text.replace(",", ""))
    unit = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div[1]/table/thead/tr/th[4]").text.split("(")[1].split("/")[0]

    if unit == "GFlop":
        rmax = rmax * 0.000001
    elif unit == "TFlop":
        rmax = rmax * 0.001

    data[year] = rmax

with open("rmax_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Year", "Rmax (PFLop/s)"])
    for year, rmax in data.items():
        writer.writerow([year, rmax])


