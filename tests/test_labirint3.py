import time
from settings import valid_email, valid_password, URL

def test_best_buy(selenium):

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на "Главное 2022":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.analytics-click-js[data-event-content="Главное"]')
    element.click()
    time.sleep(1)

    # Нажать на "Лучшая покупка"
    element = selenium.find_element_by_css_selector(
        'h2.autodiscounts__title.autodiscounts__padding>a[href="/best/sale/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот:
    selenium.save_screenshot('best_book.png')


def test_buy_book(selenium):
    # Найти в labirint книгу и переместить в корзину

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(10)

    # Найти поле для ввода текста поиска:
    search_input = selenium.find_element_by_css_selector('input#search-field.b-header-b-search-e-input')

    # Ввести текст для поиска:
    search_input.clear()
    search_input.send_keys(u"отцы и дети")
    time.sleep(3)

    # Нажать кнопку "Поиск":
    search_button = selenium.find_element_by_css_selector('button.b-header-b-search-e-btn')
    search_button.submit()
    time.sleep(5)

    # Нажать иконку "В корзину":
    element = selenium.find_element_by_css_selector('div>a#buy630372')
    element.click()
    time.sleep(1)

    # Нажать "Оформить":
    element = selenium.find_element_by_css_selector(
        'div.b-basket-popinfo-e-text-row>a')
    element.click()
    time.sleep(1)

    # Сделайте скриншот:
    selenium.save_screenshot('buy_book.png')


def test_add_2books_in_cart(selenium):
    # Найти в labirint 2 книги, поместить их в корзину, не совершая покупки, очистите корзину

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(5)

    # Найти поле для ввода текста поиска:
    search_input = selenium.find_element_by_css_selector('input#search-field.b-header-b-search-e-input')

    # Ввести текст для поиска:
    search_input.clear()
    search_input.send_keys(u"Война и мир")
    time.sleep(10)

    # Нажать кнопку "Поиск":
    search_button = selenium.find_element_by_css_selector('button.b-header-b-search-e-btn')
    search_button.submit()
    time.sleep(3)

    # Нажать иконку "В корзину":
    element = selenium.find_element_by_css_selector('div>a#buy759814')
    element.click()
    time.sleep(1)

    # Нажать "Оформить":
    element = selenium.find_element_by_css_selector('div>a#buy759814')
    element.click()
    time.sleep(1)

    # Сделайте скриншот:
    selenium.save_screenshot('book1.png')

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(10)

    # Найдите поле для ввода текста поиска:
    search_input = selenium.find_element_by_css_selector('input#search-field.b-header-b-search-e-input')

    # Введите текст для поиска:
    search_input.clear()
    search_input.send_keys(u"Преступление и наказание")
    time.sleep(3)

    # Нажмите кнопку "Поиск":
    search_button = selenium.find_element_by_css_selector('button.b-header-b-search-e-btn')
    search_button.submit()
    time.sleep(5)

    # Нажмите иконку "В корзину":
    element = selenium.find_element_by_css_selector('div>a#buy729483')
    element.click()
    time.sleep(1)

    # Нажмите "Оформить":
    element = selenium.find_element_by_css_selector('div.b-basket-popinfo-e-text-row>a')
    element.click()
    time.sleep(1)

    # Сделайте скриншот:
    selenium.save_screenshot('book2.png')

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(10)

    # Нажать на иконку "Корзина":
    element = selenium.find_element_by_css_selector('li.b-header-b-personal-e-list-item.have-dropdown.last-child')
    element.click()
    time.sleep(3)

    # Сделайте скриншот:
    selenium.save_screenshot('2books.png')


def test_club_magazines(selenium):

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на "Клуб":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.b-toggle.analytics-click-js[data-event-content="Клуб"]')
    element.click()
    time.sleep(1)

    # Нажать на "Журналы"
    element = selenium.find_element_by_css_selector(
        'a.mm-link.mm-link-big.mm-link-big-m-sub[href="/journals/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот:
    selenium.save_screenshot('magazines.png')


def test_club_now(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Клуб":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.b-toggle.analytics-click-js[data-event-content="Клуб"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Лабиринт. Сейчас"
    element = selenium.find_element_by_css_selector(
        'a.mm-link.mm-link-big.mm-link-big-m-sub[href="/now/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот:
    selenium.save_screenshot('club_now.png')


def test_children_navigator(selenium):
    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на "Клуб":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.b-toggle.analytics-click-js[data-event-content="Клуб"]')
    element.click()
    time.sleep(1)

    # Нажать на "Детский навигатор"
    element = selenium.find_element_by_css_selector(
        'a.mm-link.mm-link-big.mm-link-big-m-sub[href="/child-now/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот:
    selenium.save_screenshot('children_navigator.png')

# path: python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_labirint3.py
