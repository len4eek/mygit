from selenium import webdriver
import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    wait = WebDriverWait(browser, 15)
    form1 = browser.find_element_by_css_selector('#price').text
    print(form1)
    price = wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    #els = browser.find_elements_by_tag_name("input")
    #for el in els:
    #    el.send_keys("123")
    browser.find_element_by_id('book').click()
    e = browser.find_element_by_css_selector("#input_value.nowrap").text
    form = browser.find_element_by_id("answer")
    e = int(e)
    form.send_keys(calc(e))
    button1 = browser.find_element_by_css_selector("#solve.btn")
    button1.click()
finally:

    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла
