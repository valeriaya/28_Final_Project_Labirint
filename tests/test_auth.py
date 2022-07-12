import time
from settings import valid_email, valid_password, URL
import pytest
from selenium import webdriver


driver = webdriver.Chrome(executable_path=r'.\tests\chromedriver.exe')


@pytest.fixture(autouse=True)
def test():
    # Cтраница авторизации
    driver.get(URL)
    yield
    driver.quit()


def test_auth(web_browser):
    # Главная страница labirint:
    web_browser.get(URL)
    time.sleep(5)

    # Кликнуть на "Мой Лабиринт":
    element = web_browser.find_element_by_css_selector(
        'li.b-header-b-personal-e-list-item.have-dropdown.b-header-b-personal-e-list-item_cabinet')
    element.click()
    time.sleep(5)

    # Ввод email:
    email_box = web_browser.find_element_by_css_selector('input.full-input__input.formvalidate-error')
    email_box.clear()
    email_box.send_keys(valid_email)
    time.sleep(5)

    # Нажать кнопку "Войти":
    search_btn = web_browser.find_element_by_css_selector('input#g-recap-0-btn')
    search_btn.submit()
    time.sleep(5)

    #  Ввести код скидки (пароль)
    password_box = web_browser.find_element_by_css_selector('input[placeholder="Введите свой код скидки"]')
    password_box.clear()
    password_box.send_keys(valid_password)

    # Нажать кнопку "Проверить код и войти":
    search_btn = web_browser.find_element_by_css_selector('input[data-default-value="Проверить код и войти"]')
    search_btn.submit()
    time.sleep(5)

    # Сделать скриншот личного кабинета:
    web_browser.save_screenshot('lk.png')


#  path: python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_auth.py