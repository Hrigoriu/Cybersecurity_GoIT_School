import os
from dotenv import load_dotenv
from openai import OpenAI
from dormouse import DormouseClient
from typing import Any

# 1. Завантаження та перевірка ключа
load_dotenv()
# Отримуємо ключ і ВІДРАЗУ чистимо його від пробілів та переносів
api_key = os.getenv("OPENAI_API_KEY", "").strip()

if not api_key:
    print("❌ ПОМИЛКА: Ключ не знайдено в .env")
    exit()

# Виводимо частину ключа для перевірки (можна видалити після успіху)
print(f"DEBUG: Ключ завантажено успішно. Початок: {api_key[:10]}...")

# 2. Ініціалізація (виконуємо один раз!)
try:
    # Створюємо базовий клієнт із очищеним ключем
    base_client = OpenAI(api_key=api_key)
    # Огортаємо його в Dormouse для економії токенів
    client = DormouseClient(base_client)
except Exception as e:
    print(f"❌ Помилка ініціалізації клієнта: {e}")
    exit()

# 3. Виконання запиту
print("🚀 Надсилаю оптимізований запит...")

try:
    response: Any = client.chat.completions.create(
       model="gpt-4o-mini",
       messages=[{"role": "user", "content": "Поясни що таке трансформери"}]
   )

    print("\n--- Відповідь AI (через Dormouse) ---")
    print(response.choices[0].message.content)

except Exception as e:
    # Якщо тут знову 401 — це 100% проблема балансу акаунту або прав ключа
    print(f"❌ Помилка при виконанні запиту: {e}")
