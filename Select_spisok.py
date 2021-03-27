from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math



try:
    #Считакм пример из капчи
    def calc(x,y):
        return str(x+y)

    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ищем значение x для примера
    x_find=browser.find_element_by_id('num1')
    x=x_find.text
    x=int(x)
    # ищем значение y
    y_find=browser.find_element_by_id('num2')
    y=y_find.text
    y=int(y)


    #Считаем нашу функцию
    rez=calc(x,y)

    #Выбираем значение из выпадающего списка
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(rez)

    button = browser.find_element_by_css_selector('.btn.btn-default')
    button.click()




    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
     time.sleep(5)
    # закрываем браузер после всех манипуляций
     browser.quit()