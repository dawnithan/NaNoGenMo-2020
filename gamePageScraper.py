from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random

# path
driver_path = 'D:\\chromedriver_win32\\chromedriver.exe'

# set up webdriver
options = Options()
options.headless = True
options.add_argument("--enable-javascript")

driver = webdriver.Chrome(executable_path=driver_path, options=options)

long_descriptions = set()
link_sample = set()

with open("links.txt", "r") as f:
    lines = f.readlines()

    for i in range(50):
        link_sample.add(random.choice(lines))

    # print(link_sample)

    for link in link_sample:
        driver.get(link)
        soup = BeautifulSoup(driver.page_source, 'lxml')

        try:
            description = soup.find(class_="formatted_description user_formatted")
            desc_text = description.find_all("p")
            for p in desc_text:
                # print(p.get_text())
                long_descriptions.add(p.get_text() + "\n")
        except:
            print("error finding description at " + link)
    # print(desc_text)

with open("long-descriptions.txt", "a", encoding="utf8") as f:
    f.writelines(long_descriptions)