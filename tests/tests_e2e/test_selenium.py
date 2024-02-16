from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from peewee import PostgresqlDatabase

from spectehnika.auth.models import User, Owner, Report, MachineTypes, Machine, Role

current_user: User


def test_wrong_auth(driver: webdriver.Chrome):
    driver.get('http://127.0.0.1:5000/auth/login')
    email = driver.find_element(By.ID, 'email')
    email.send_keys('spalm@list.ru')
    password = driver.find_element(By.ID, 'password')
    password.send_keys('1111')
    password.send_keys(Keys.RETURN)

    wait = WebDriverWait(driver, timeout=3)
    wait.until(presence_of_element_located((By.CSS_SELECTOR, 'span[class="tag is-danger is-light"]')))

    danger_tag = driver.find_element(By.CSS_SELECTOR, 'span[class="tag is-danger is-light"]')
    assert danger_tag.text == 'Неверный email или пароль'


def test_success_admin_page(driver: webdriver.Chrome, db: PostgresqlDatabase):
    print(User._meta.database)
    driver.get('http://127.0.0.1:5000/auth/login')
    email = driver.find_element(By.ID, 'email')
    email.send_keys('spalm@list.ru')
    password = driver.find_element(By.ID, 'password')
    password.send_keys('0000')
    password.send_keys(Keys.RETURN)

    start_employee_quantity = len(User.select())
    assert start_employee_quantity == 3

    wait = WebDriverWait(driver, timeout=3)
    wait.until(presence_of_element_located(
        (By.CSS_SELECTOR, 'a[href="/emp/employees"]'))
    )
    clickable = driver.find_element(By.CSS_SELECTOR, 'a[href="/emp/employees"]')
    ActionChains(driver).click(clickable).perform()
    wait = WebDriverWait(driver, timeout=3)
    wait.until(presence_of_element_located((By.ID, 'add_employee')))

    name = driver.find_element(By.ID, 'name')
    name.send_keys('Мария')
    email = driver.find_element(By.ID, 'email')
    email.send_keys('maria@mail.ru')

    password = driver.find_element(By.ID, 'password')
    password.send_keys('1010')

    select_element = driver.find_element(By.NAME, 'role')
    select = Select(select_element)
    select.select_by_visible_text('Менеджер')

    password.send_keys(Keys.RETURN)
    #TODO: Добавить задержку
    finish_employee_quantity = len(User.select())
    assert finish_employee_quantity == 4
    # assert len(User.select().where(User.email == "maria@mail.ru")) == 1

