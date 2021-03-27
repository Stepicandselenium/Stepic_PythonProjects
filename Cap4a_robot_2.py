from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math



try:
    #Считакм пример из капчи
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ищем значение x для примера
    x_find=browser.find_element_by_id('input_value')
    x=x_find.text





    #Считаем нашу функцию
    rez=calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    answer=browser.find_element_by_tag_name('input')
    answer.send_keys(rez)

    check_box=browser.find_element_by_id('robotCheckbox')
    check_box.click()

    redio_butoon=browser.find_element_by_id("robotsRule")
    redio_butoon.click()



    button = browser.find_element_by_css_selector('.btn.btn-primary')
    button.click()




    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
     time.sleep(5)
    # закрываем браузер после всех манипуляций
     browser.quit()