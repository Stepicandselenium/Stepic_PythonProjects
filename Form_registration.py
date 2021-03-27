from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_nessasary1 = browser.find_element_by_css_selector('div.first_class >:nth-child(2)')
    input_nessasary1.send_keys('Vladislav')
    input_nessasary2=browser.find_element_by_css_selector('.first_block >:nth-child(2)>.second')
    input_nessasary2.send_keys('Abramovich')
    input_nessasary3=browser.find_element_by_css_selector('.third_class  :nth-child(2)')
    input_nessasary3.send_keys('NOWDAYS@gmail.com')



    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()