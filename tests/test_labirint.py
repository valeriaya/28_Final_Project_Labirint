import time
from settings import valid_email, valid_password, URL


def test_auth(selenium):
    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Мой Лабиринт":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-personal-e-list-item.have-dropdown.b-header-b-personal-e-list-item_cabinet')
    element.click()
    time.sleep(1)

    # Введите email:
    email_field = selenium.find_element_by_css_selector('input.full-input__input.formvalidate-error')
    email_field.clear()
    email_field.send_keys(valid_email)
    time.sleep(1)

    # Нажмите кнопку "Войти":
    search_button = selenium.find_element_by_css_selector('input#g-recap-0-btn')
    search_button.submit()
    time.sleep(1)

    #  Введите код скидки ("password")
    password_field = selenium.find_element_by_css_selector('input[placeholder="Введите свой код скидки"]')
    password_field.clear()
    password_field.send_keys(valid_password)

    # Нажмите кнопку "Проверить код и войти":
    search_button = selenium.find_element_by_css_selector('input[data-default-value="Проверить код и войти"]')
    search_button.submit()
    time.sleep(5)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('lk.png')
    # assert page.get_current_url() == URL + '/cabinet'


def test_authgoogle(selenium):
    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(3)

    # Нажать на элемент "Сообщения":
    element = selenium.find_element_by_css_selector(
        'a.b-header-b-personal-e-link.top-link-main.have-dropdown-touchlink.top-link-main_notification')
    element.click()

    # Нажать на элемент "Другие способы входа":
    element = selenium.find_element_by_css_selector('div.new-auth__show-soc')
    element.click()

    # Нажать на иконку "Google":
    element = selenium.find_element_by_css_selector(
        'span.new-auth__auth-social__text.header-sprite.new-auth__auth-social_gl')
    element.click()

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('auth-google.png')


def test_elem_books(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)
    # Нажать на элемент "Книги":
    element = selenium.find_element_by_css_selector(
        'span.b-header-b-menu-e-link.top-link-menu.first-child>a')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('books.png')


def test_search_book(selenium):

    # Найдите в labirint книгу и сделайте скриншот страницы

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(10)

    # Найдите поле для ввода текста поиска:
    search_input = selenium.find_element_by_css_selector('input#search-field.b-header-b-search-e-input')

    # Введите текст для поиска:
    search_input.clear()
    search_input.send_keys(u"Шерлок Холмс")

    time.sleep(5)

    # Нажмите кнопку Поиск:
    search_button = selenium.find_element_by_css_selector('button.b-header-b-search-e-btn')
    search_button.submit()
    time.sleep(5)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('book.png')


def test_page_main2022(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)
    # Нажать на элемент "Главное 2022":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.analytics-click-js[data-event-content="Главное"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('page_2022.png')


def test_page_deliveryandpay(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(3)
    # Нажать на элемент "Доставка и оплата":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-sec-menu-e-list-item.first-child.analytics-click-js')
    element.click()

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('deliv.png')


def test_page_cert(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(3)
    # Нажать на элемент "Сертификаты":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-sec-menu-e-list-item.analytics-click-js[data-event-content="Сертификаты"]')
    element.click()

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('cert.png')


def test_page_ratings(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(3)
    # Нажать на элемент "Рейтинги":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-sec-menu-e-list-item.analytics-click-js[data-event-content="Рейтинги"]')
    element.click()

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('ratings.png')


def test_page_new_books(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(3)
    # Нажать на элемент "Новинки":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-sec-menu-e-list-item.analytics-click-js[data-event-content="Новинки"]')
    element.click()

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('newbooks.png')


def test_discount(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(3)
    # Нажать на элемент "Скидки":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-sec-menu-e-list-item.analytics-click-js[data-event-content="Скидки"]')
    element.click()

    # Сделайте скриншот:
    selenium.save_screenshot('discount.png')



def test_applications_reviews(selenium):

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

    # Нажать на "Заявки на рецензии"
    element = selenium.find_element_by_css_selector(
        'li.b-stab-e-slider-item>a[href="/reviews/applications"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот:
    selenium.save_screenshot('applications.png')


def test_review_authors(selenium):

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

    # Нажать на "Авторы рецензий"
    element = selenium.find_element_by_css_selector(
        'li.b-stab-e-slider-item>a[href="/reviews/users"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот:
    selenium.save_screenshot('review_authors.png')


# path: python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_labirint.py