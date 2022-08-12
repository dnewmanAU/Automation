from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium import webdriver
import pandas as pd

# browser and driver version must match
options = Options()
options.binary_location = (
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
)
service = Service(
    executable_path=r"C:\Users\davev\Documents\edgedriver_win64\msedgedriver.exe"
)
driver = webdriver.Edge(options=options, service=service)
driver.maximize_window()
driver.get("https://www.abc.net.au/news/justin")

titles = []
descriptions = []
links = []

containers = driver.find_elements(
    by="xpath", value='//div[@class="_16eiR"]'
)

print(containers)

for container in containers:
    titles.append(
        container.find_element(
            by="xpath", value='./h3/span/a'
        ).text
    )
    descriptions.append(
        container.find_element(
            by="xpath", value='.//div[@data-component="CardDescription"]'
        ).text
    )
    links.append(
        container.find_element(
            by="xpath", value='./h3/span/a'
        ).get_attribute("href")
    )

df_news_headlines = pd.DataFrame(
    {"Title": titles, "Descrtiption": descriptions, "Link": links}
)

df_news_headlines.to_csv("news-headlines.csv")

driver.quit()
