import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    service = Service(executable_path='../../utils/chromedriver.exe')
    return webdriver.Chrome(service=service)
