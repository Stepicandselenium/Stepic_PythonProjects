from selenium import webdriver
import time
import math



try:
    #Считакм пример из капчи
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x=x_element.text
    y=calc(x)

    answer=browser.find_element_by_id('answer')
    answer.send_keys(y)

    option_checkbox=browser.find_element_by_css_selector('[for=robotCheckbox]')
    option_checkbox.click()

    option_radiobutton=browser.find_element_by_css_selector('[for=robotsRule]')
    option_radiobutton.click()

    button=browser.find_element_by_css_selector('.btn.btn-default')
    button.click()




    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
     time.sleep(5)
    # закрываем браузер после всех манипуляций
     browser.quit()