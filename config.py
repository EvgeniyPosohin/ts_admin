import os
from dotenv import load_dotenv, dotenv_values


# Подгружаем из переменных окружения, локально будут храниться токены в файл .env
load_dotenv()
data = dotenv_values()

