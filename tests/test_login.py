from pages.login_page import LoginPage


def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Проверяем, что мы попали на страницу товаров (URL изменился)
    assert page.url == "https://www.saucedemo.com/inventory.html"


def test_locked_out_user(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("locked_out_user", "secret_sauce")

    # Проверяем, что появилось сообщение об ошибке
    error_text = login_page.error_message.inner_text()
    assert "Sorry, this user has been locked out" in error_text