# переменные окружения
# python-dotenv нужен для настройки переменных окружения

# Для передачи токена создайте файл .env со следующим содержимым
# TOKEN=ВАШ_ТОКЕН

import os
from dotenv import load_dotenv

load_dotenv()

TOKEN: str = os.getenv('TOKEN')

