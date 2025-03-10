from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

# URL-ы для переходов
product_url = "https://www.wildberries.ru/catalog/168512865/detail.aspx"
search_url = "https://www.wildberries.ru/"

# Настройка опций для Chrome
chrome_options = Options()
# Если нужно запускать в фоновом режиме, раскомментируй следующую строку
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# Инициализация драйвера (убедиcь, что chromedriver находится в PATH или укажи путь к нему)
driver = webdriver.Chrome(options=chrome_options)

try:
    while True:
        # 1. Переход на страницу карточки товара
        try:
            driver.get(product_url)
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{current_time}] Переход на карточку товара удачный")
        except Exception as e:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{current_time}] Переход на карточку товара не удался по причине {str(e)}")

        # Задержка в 1 секунду
        time.sleep(10)

        # 2. Переход на страницу поиска
        try:
            driver.get(search_url)
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{current_time}] Переход на страницу поиска удачный")
        except Exception as e:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{current_time}] Переход на страницу поиска не удался по причине {str(e)}")

        # Минимальная задержка перед следующим циклом
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Бот остановлен пользователем.")
finally:
    driver.quit()
