from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    one = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary")
    one.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, value="[type='submit']")
    button.click()
    print(browser.switch_to.alert.text)


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла