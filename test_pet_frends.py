#30.5.1 В написанном тесте (проверка карточек питомцев) добавьте неявные ожидания всех элементов
# (фото, имя питомца, его возраст).

import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from settings import valid_email, valid_password


@pytest.fixture(autouse=True)
def testing():
    global driver  # объявление переменной driver как глобальной
    options = webdriver.ChromeOptions()
    options.add_argument('./chromedriver.exe')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get('https://petfriends.skillfactory.ru/login')
    yield
    driver.quit()


def test_pet_friends():
    """Проверка карточек питомцев всех пользователей
    на наличие фото, имени и описания (порода и возраст)"""

    global driver  # объявление переменной driver как глобальной

    # Ввод эл.почты
    driver.find_element(By.ID, 'email').send_keys(valid_email)

    # Ввод пароля
    driver.find_element(By.ID, 'pass').send_keys(valid_password)

    # Клик по кнопке "Войти"
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Проверка того, что осуществлен переход на главную страницу пользователя
    assert driver.current_url == 'https://petfriends.skillfactory.ru/all_pets'

    images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    assert names[0].text != ''

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ',' in descriptions[i].text
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0