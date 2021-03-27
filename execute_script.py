from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math




try:


    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector('.btn.btn-primary')
    button.click()

    confirm=browser.switch_to.alert
    confirm.accept()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_find=browser.find_element_by_id('input_value')
    x=x_find.text

    rez=calc(x)

    answer=browser.find_element_by_id('answer')
    answer.send_keys(rez)

    button = browser.find_element_by_css_selector('.btn.btn-primary').click()









    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
     time.sleep(5)
    # закрываем браузер после всех манипуляций
     browser.quit()