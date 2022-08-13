import os
import sys
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

# Note: browser and driver version must match
edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
driver_path = "C:/Users/davev/Documents/edgedriver_win64/msedgedriver.exe"
url = "https://www.abc.net.au/news/justin"

titles = []
descriptions = []
links = []

time = datetime.now().strftime("%d%m%Y")  # ddmmyyyy
app_path = os.path.dirname(sys.executable)

# Headless mode
options = Options()
options.headless = True
options.binary_location = edge_path
service = Service(executable_path=driver_path)
driver = webdriver.Edge(options=options, service=service)
driver.maximize_window()
driver.get(url)

containers = driver.find_elements(by="xpath", value='//div[@class="_16eiR"]')

for container in containers:
    titles.append(container.find_element(by="xpath", value="./h3/span/a").text)
    descriptions.append(
        container.find_element(
            by="xpath", value='.//div[@data-component="CardDescription"]'
        ).text
    )
    links.append(
        container.find_element(by="xpath", value="./h3/span/a").get_attribute("href")
    )

df_news_headlines = pd.DataFrame(
    {"Title": titles, "Descrtiption": descriptions, "Link": links}
)
csv_name = f"news-headlines-{time}.csv"
csv_path = os.path.join(app_path, csv_name)
df_news_headlines.to_csv(csv_path)

driver.quit()
