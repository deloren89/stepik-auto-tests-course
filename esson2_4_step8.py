from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

# Описать функцию
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Открыть страницу
link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Firefox()
browser.get(link) 


# Дождаться, когда цена дома уменьшится до 100 USD 
prise = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

# Нажать на кнопку Забронировать
button_book = browser.find_element_by_id("book")
button_book.click()

# неявное ожидание появления элементов
browser.implicitly_wait(5)

# Считать значение x 
x_element = browser.find_element_by_css_selector('[id="input_value"]')
x = x_element.text

# Расcчитать значение функции
y = calc(x)

# Ввести ответ в текстовое поле
answer = browser.find_element_by_id('answer')
answer.send_keys(y)

# Нажать на кнопку Отправить
button_solve = browser.find_element_by_id("solve")
button_solve.click()
