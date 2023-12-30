from selenium.webdriver.common.by import By
import time # добавлен сразу для вашего удобства

def test_presence_add_to_cart_button(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    time.sleep(15)
    
    assert search_element(browser, "btn.btn-lg.btn-primary.btn-add-to-basket"), 'Кнопка "добавить в корзину" не найдена'

# простенький обработчик ошибок проверяющий наличие кнопки 
def search_element(browser, class_name: str) -> bool:
    try: 
        browser.find_element(By.CLASS_NAME, class_name) 
        return True
    except:
        return False