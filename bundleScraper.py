from credentials import data
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# paths & urls
driver_path = 'D:\\chromedriver_win32\\chromedriver.exe'
login_url = 'https://itch.io/login'
bundle_url = 'https://itch.io/bundle/download/<your_bundle_url>'

# set up webdriver
options = Options()
options.headless = True
options.add_argument("--enable-javascript")

driver = webdriver.Chrome(executable_path=driver_path, options=options)
driver.get(login_url)

# login to itch.io
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
username.send_keys(data['username'])
password.send_keys(data['password'])

buttons = driver.find_element_by_class_name("buttons")
buttons.find_element_by_class_name("button").click()

# access the bundle page
driver.get(bundle_url)

game_urls = set()
game_descriptions = set()
end_punctuation = ('!','?','.')

for i in range(58):
    soup = BeautifulSoup(driver.page_source, 'lxml')
    game_list = soup.find_all(class_="game_row")

    for game in game_list:
        link = game.findChild('a')['href']
        game_urls.add(link + '\n')

        desc = game.findChild(class_="meta_row game_short_text").get_text()

        if not desc.endswith(end_punctuation):
            desc += '.'
        
        desc += ' '
        game_descriptions.add(desc)

    driver.find_element_by_class_name("next_page").click()

with open("short-descriptions.txt", "w", encoding="utf8") as f:
    f.writelines(game_descriptions)

with open("links.txt", "w", encoding="utf8") as f:
    f.writelines(game_urls)

# print(game_urls)
# print(game_descriptions)

driver.quit()