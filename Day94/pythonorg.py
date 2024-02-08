from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

list_items_dates = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/time')
list_items_events = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/a')
result_dict = {}

for i in range(0, len(list_items_dates)):
    result_dict[i] = {
        "time": list_items_dates[i].text,
        "name": list_items_events[i].text
    }

print(result_dict)
driver.quit()

# //*[@id="content"]/div/section/div[3]/div[2]/div/ul

