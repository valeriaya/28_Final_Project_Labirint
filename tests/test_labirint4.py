import time
from settings import URL

def test_number_reviews(selenium):

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на "Клуб":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.b-toggle.analytics-click-js[data-event-content="Клуб"]')
    element.click()
    time.sleep(1)

    # Нажать на "Рецензии читателей"
    element = selenium.find_element_by_css_selector(
        'li.top-main-menu-item>a[href="/reviews/"]')
    element.click()
    time.sleep(1)

    # Нажать на "Количество рецензий"
    element = selenium.find_element_by_css_selector(
        'li.b-stab-e-slider-item.b-stab-e-slider-item-m-active>a')
    element.click()
    time.sleep(2)

    # Сделайте скриншот:
    selenium.save_screenshot('number_reviews.png')


def test_postponed(selenium):

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на иконку "Отложено":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-personal-e-list-item.have-dropdown>a[href="/cabinet/putorder/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот:
    selenium.save_screenshot('postponed.png')


def test_postponed_main_books(selenium):

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на иконку "Отложено":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-personal-e-list-item.have-dropdown>a[href="/cabinet/putorder/"]')
    element.click()
    time.sleep(1)

    # Нажать на "Главные книги":
    element = selenium.find_element_by_css_selector(
        'div#cabinet>div>span>a[href="/best/"]')
    element.click()
    time.sleep(1)

    # Сделать скриншот:
    selenium.save_screenshot('main_books.png')


def test_postponed_discounts_gifts(selenium):

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на иконку "Отложено":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-personal-e-list-item.have-dropdown>a[href="/cabinet/putorder/"]')
    element.click()
    time.sleep(1)

    # Нажать на "Скидки и подарки":
    element = selenium.find_element_by_css_selector(
        'div#cabinet>div>span>a[href="/search/?discount=1&available=1&wait=1&no=1&order=actd&way=back"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот:
    selenium.save_screenshot('discounts_gifts.png')


def test_basket(selenium):

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на иконку "Корзина":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-personal-e-list-item.have-dropdown.last-child')
    element.click()
    time.sleep(1)

    # Сделайте скриншот:
    selenium.save_screenshot('cart.png')


def test_put_aside(selenium):

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на иконку "Корзина":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-personal-e-list-item.have-dropdown.last-child')
    element.click()
    time.sleep(1)

    # Нажать на иконку "Отложенные":
    element = selenium.find_element_by_css_selector(
        'li.ui-state-default.ui-corner-top>a[href="#step1-put"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот:
    selenium.save_screenshot('putaside.png')


def test_what_to_read(selenium):

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на "Что почитать?":
    element = selenium.find_element_by_css_selector(
        'span.b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long')
    element.click()
    time.sleep(1)

    # Сделайте скриншот:
    selenium.save_screenshot('recommend.png')


# path: python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_labirint4.py