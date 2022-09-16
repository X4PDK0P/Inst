from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import random


# Данные для авторизации
Login = 'vasiapupkin2077'
Password = 'ASDFGHJKLqwertyuiop0'
# Настройки браузера
options = webdriver.ChromeOptions()
# Фоновый режим
# options.add_argument('--headless')
# Работа браузера
browser = webdriver.Chrome(executable_path='D:\\Project\\Browser\\chromedriver.exe', options=options)
browser.get('https://www.instagram.com/')


def login(Login, Password):
    time.sleep(random.randrange(3, 5))
    browser.find_element_by_name('username').clear()
    browser.find_element_by_name('username').send_keys(Login)
    time.sleep(random.randrange(1, 3))
    browser.find_element_by_name('password').clear()
    time.sleep(random.randrange(0, 1))
    browser.find_element_by_name('password').send_keys(Password, Keys.ENTER)
    time.sleep(random.randrange(3, 5))
    # Закрытие всплывающего окна "Позже"
    try:
        browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    except:
        pass


def search(tag):
    browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').clear()
    browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(tag)
    time.sleep(random.randrange(1, 3))
    browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(Keys.ARROW_DOWN, Keys.ENTER)
    time.sleep(random.randrange(3, 5))


def like():
    global st, fn
    fn = int(input(f'{st} Конечное значение'))
    hrefs = browser.find_elements_by_tag_name('a')
    print(hrefs)
    post_urls = [item.get_attribute('href') for item in hrefs if '/p/' in item.get_attribute('href')]
    print(post_urls)
    for url in post_urls[st:fn]:
        try:
            browser.get(url)
            time.sleep(random.randrange(2, 4))
            browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
            time.sleep(random.randrange(90, 120))
            st = fn
        except Exception as ex:
            print(ex)


def close_browser():
    browser.close()
    browser.quit()


try:
    login(Login, Password)
    tag = '#маслодлядерева'#tag = input('Введите хештег \n')
    search(tag)
    i = 1
    while i != 0:
        st = 0
        like()
    time.sleep(10)
except Exception as ex:
    print(ex)
    close_browser()
finally:
    close_browser()
