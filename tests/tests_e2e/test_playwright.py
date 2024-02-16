import pytest
from playwright.sync_api import Page, expect, Playwright, sync_playwright

from auth.models import User, Machine


def authorize(page: Page):
    page.goto('http://127.0.0.1:5000/')
    page.get_by_label('Email').fill('spalm@list.ru')
    page.get_by_label('Пароль').fill('0000')
    page.get_by_role('button', name='Войти').click()


def test_test(page: Page):
    authorize(page)
    page.screenshot(path='after_login.png')
    expect(page).to_have_title('Главная страница администратора')


def test_add_employee(page: Page, db):
    authorize(page)
    page.goto('http://127.0.0.1:5000/emp/employees')
    page.screenshot(path='before_add_employee.png')
    assert User._meta.database.database.endswith('_test')
    page.get_by_label('имя').fill('Мария')
    page.get_by_label('должность').select_option('Менеджер')
    page.get_by_label('почта').fill('maria@spectehnika.ru')
    page.get_by_label('пароль').fill('1111')
    page.get_by_role('button', name='Добавить').click()
    page.screenshot(path='after_add_employee.png')

    assert User.get(User.email == 'maria@spectehnika.ru') is not None


def test_success_add_type_machine(page: Page, playwright: Playwright) -> None:
    authorize(page)
    page.goto('http://127.0.0.1:5000/teh/tehnika')
    page.get_by_label("тип техники").fill("что-то")
    page.locator("#add_type").get_by_role("button", name="Добавить").click()
    notification = page.get_by_text("Тип добавлен успешно")

    assert notification is not None


# def test_fault_add_type_machine(page: Page, playwright: Playwright) -> None:
#     authorize(page)
#     page.goto('http://127.0.0.1:5000/teh/tehnika')
#     page.get_by_label("тип техники").fill("что-то")
#     page.locator("#add_type").get_by_role("button", name="Добавить").click()
#     page.get_by_label("тип техники").fill("что-то")
#     page.locator("#add_type").get_by_role("button", name="Добавить").click()
#     notification = page.get_by_text("Машина с таким номером уже есть")
#
#     assert notification is not None


def test_success_add_machine(page: Page, playwright: Playwright) -> None:
    authorize(page)
    page.goto('http://127.0.0.1:5000/teh/tehnika')
    page.get_by_label("тип техники").fill("Мини-экскаватор")
    page.locator("#add_type").get_by_role("button", name="Добавить").click()

    page.get_by_label("модель").click()
    page.get_by_label("модель").fill("LonKing 4026")
    page.get_by_label("тип", exact=True).select_option("4")
    page.get_by_label("гос номер").click()
    page.get_by_label("гос номер").fill("7777рт78")
    page.get_by_label("машинист").select_option("3")
    page.locator("#add_tehnika").get_by_role("button", name="Добавить").click()

    assert len(Machine.select()) == 4