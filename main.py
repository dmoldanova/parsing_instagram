from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common import exceptions
from selenium.webdriver.common.action_chains import ActionChains
import time

WINDOW_SIZE = "1920,1080"
# установка дескриптора (открытие браузера)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

#driver = webdriver.Chrome(chrome_options)
driver = webdriver.Chrome()

# вход в Instagram
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
time.sleep(3)
    # login
login = driver.find_elements_by_css_selector('._2hvTZ.pexuQ.zyHYP')
print(len(login))
login[0].click()
login[0].send_keys('')
    # password
print(len(login))
login[1].click()
login[1].send_keys('')
    # input
button = driver.find_elements_by_css_selector('._0mzm-.sqdOP.L3NKy')
button[0].click()
time.sleep(7)

# загружаем какую-нибудь страницу из инсты
driver.get("https://www.instagram.com/dasha.moldanova/")
#body = driver.find_element_by_id('react-root')
time.sleep(4)
substractions = driver.find_elements_by_css_selector('.v9tJq')
print(len(substractions))
s = substractions[0].find_elements_by_tag_name('li')
print(len(s))
s[2].click()
time.sleep(5)
count_substractions = s[2].find_element_by_tag_name("span").text
print('count_substractions: ', count_substractions)
i = 0

while i < int(count_substractions):
    print('-------- {} ---------'.format(i))
    sub = driver.find_elements_by_css_selector('.isgrP')
    print('Count sub: ', len(sub))
    body_sub = sub[0].find_elements_by_tag_name("li")
    print('Count body_sub: ', len(body_sub))
    div_body_sub = body_sub[11].find_elements_by_tag_name("div")
    print('Div body sub: ', len(div_body_sub))
    #print('Name: ', div_body_sub[6].text, '(', div_body_sub[7].text, ')')
    print('=====')
    for j in range(i, len(body_sub), 1):
        print('{} --> {}'.format(j, body_sub[j].text))
    print('=====')
    actions = ActionChains(driver)
    actions.move_to_element(body_sub[i-1])
    actions.click()
    actions.send_keys(Keys.END)
    actions.perform()
    i = len(body_sub)
    time.sleep(3)

'''
try:
    print('FIRST')
    body_sub[0].send_keys(Keys.END)
except exceptions.WebDriverException:
    print('SECOND')
    body_sub[0].send_keys(Keys.END)
time.sleep(4)
'''
