import time
from settings import valid_email, valid_password, URL


def test_page_contacts(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(3)
    # Нажать на элемент "Контакты":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-sec-menu-e-list-item.analytics-click-js[data-event-content="Контакты"]')
    element.click()

    # Сделайте скриншот:
    selenium.save_screenshot('contacts.png')


def test_support(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(3)
    # Нажать на элемент "Поддержка":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-sec-menu-e-list-item.analytics-click-js[data-event-content="Поддержка"]')
    element.click()

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('support.png')


def test_page_export(selenium):

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(3)
    # Нажать на элемент "2527 пункта самовывоза":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-sec-menu-e-list-item.last-child.analytics-click-js[data-event-content="Пункты самовывоза"]')
    element.click()

    # Сделайте скриншот :
    selenium.save_screenshot('export.png')


def test_messages(selenium):

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(3)

    # Нажать на элемент "Сообщения":
    element = selenium.find_element_by_css_selector(
        'a.b-header-b-personal-e-link.top-link-main.have-dropdown-touchlink.top-link-main_notification')
    element.click()

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('message.png')


def test_book_type(selenium):

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(3)

    # Нажать на элемент "Книги":
    element = selenium.find_element_by_css_selector(
        'span.b-header-b-menu-e-link.top-link-menu.first-child>a')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Тип товара"
    element = selenium.find_element_by_css_selector(
        'span.navisort-part.navisort-filter.navisort-part-1.fleft')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('book_type.png')


def test_all_book(selenium):

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на "Главное 2022":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.analytics-click-js[data-event-content="Главное"]')
    element.click()
    time.sleep(1)

    # Нажать на "Все книги"
    element = selenium.find_element_by_css_selector(
        'li.swiper-slide.selected.swiper-slide-active')
    element.click()
    time.sleep(1)

    # Сделайте скриншот:
    selenium.save_screenshot('all_books.png')


def test_discounts_today(selenium):

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на "Главное 2022":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.analytics-click-js[data-event-content="Главное"]')
    element.click()
    time.sleep(1)

    # Нажать на "Скидки сегодня"
    element = selenium.find_element_by_css_selector(
        'li.swiper-slide.swiper-slide-next')
    element.click()
    time.sleep(1)

    # Сделайте скриншот:
    selenium.save_screenshot('discounts.png')


def test_books_children(selenium):

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на "Главное 2022":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.analytics-click-js[data-event-content="Главное"]')
    element.click()
    time.sleep(1)

    # Нажать на "Детям"
    element = selenium.find_element_by_css_selector(
        'li.swiper-slide>a[href="/best/kids/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот:
    selenium.save_screenshot('children.png')


def test_page_fiction(selenium):

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Главное 2022":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.analytics-click-js[data-event-content="Главное"]')
    element.click()
    time.sleep(5)

    # Нажать на элемент "Художественная литература"
    element = selenium.find_element_by_css_selector(
        'li.swiper-slide>a[href="/best/fiction/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('fiction.png')


def test_page_nonfiction(selenium):

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на "Главное 2022":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.analytics-click-js[data-event-content="Главное"]')
    element.click()
    time.sleep(1)

    # Нажать на "Нонфикшн"
    element = selenium.find_element_by_css_selector(
        'li.swiper-slide>a[href="/best/nonfiction/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('nonfiction.png')


def test_gift_editions(selenium):

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на "Главное 2022":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.analytics-click-js[data-event-content="Главное"]')
    element.click()
    time.sleep(1)

    # Нажать на "Подарочные издания"
    element = selenium.find_element_by_css_selector(
        'li.swiper-slide>a[href="/best/giftbooks/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот:
    selenium.save_screenshot('editions.png')


def test_book_review(selenium):

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на "Клуб":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.b-toggle.analytics-click-js[data-event-content="Клуб"]')
    element.click()
    time.sleep(5)

    # Нажать на "Книжные обзоры"
    element = selenium.find_element_by_css_selector(
        'a.mm-link.mm-link-big.mm-link-big-m-sub[href="/news/books/"]')
    element.click()
    time.sleep(5)

    # Сделать скриншот окна браузера:
    selenium.save_screenshot('reviews.png')


def test_readers_review(selenium):

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

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('readers_reviews.png')


def test_collections_of_readers(selenium):

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на "Клуб":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.b-toggle.analytics-click-js[data-event-content="Клуб"]')
    element.click()
    time.sleep(1)

    # Нажать на "Подборки читателей"
    element = selenium.find_element_by_css_selector(
        'li.top-main-menu-item>a[href="/recommendations/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот:
    selenium.save_screenshot('collections_readers.png')


def test_littests(selenium):

    # Главная страница labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на "Клуб":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.b-toggle.analytics-click-js[data-event-content="Клуб"]')
    element.click()
    time.sleep(1)

    # Нажать на "Литтесты""
    element = selenium.find_element_by_css_selector(
        'li.top-main-menu-item>a[href="/littest/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот:
    selenium.save_screenshot('littests.png')


def test_new_review(selenium):

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

    # Нажать на "Рецензии"
    element = selenium.find_element_by_css_selector(
        'li.b-stab-e-slider-item>a[href="/reviews/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот:
    selenium.save_screenshot('new_reviews.png')

# path: python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_labirint2.py