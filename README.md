# Telegram-BOT-with-FSM-aiosqlite
# Telegram Password Manager Bot with Custom Flow Validation

An asynchronous Telegram bot built with Python that operates as a secure password manager. It collects user data step-by-step using Finite State Machine (FSM), outputs a structured preview, and verifies the final decision using native Python string search algorithms before committing data to an SQLite database.

---

## 🇬🇧 English Version

### 🛠 Tech Stack:
* **Python 3.12+**
* **Aiogram 3.x** — Asynchronous framework for Telegram Bot API.
* **Aiosqlite** — Asynchronous library for SQLite database interaction.

### ⚙️ Key Features & Architecture:
1. **Isolated FSM Handlers:** Implements the core architectural rule: *one step — one handler*. It completely avoids tight coupling by eliminating recursive function forwarding (`await`), preventing input memory buffer conflicts.
2. **Native Python Validation:** Uses native Python `in` membership testing operator combined with `.lower()` string methods to securely validate the final checkout keyword regardless of text casing.
3. **Data Protection & Persistence:** Buffers input inside volatile memory (`FSMContext`) during the session, and commits it via asynchronous `INSERT` query to a permanent `user_data.db` storage on disk only after receiving explicit confirmation.
4. **Exception Handling:** User input workflows are protected against structural engine issues by dynamically resetting the lifecycle using `state.clear()` upon successful asset injection.

### 🚀 How to Run:
1. Put your bot token inside the `bot = Bot(token="...")` object.
2. Execute the python script.

---

## 🇷🇺 Russian Version / Русская версия

### 🛠 Технологический стек:
* **Python 3.12+**
* **Aiogram 3.x** — асинхронный фреймворк для Telegram Bot API.
* **Aiosqlite** — асинхронная библиотека для работы с базой данных SQLite.

### ⚙️ Основные фичи и архитектура:
1. **Изолированные хэндлеры FSM:** Реализует главное правило архитектуры: *один шаг — один хэндлер*. Код полностью избавлен от жесткой связанности функций через `await`, что исключает конфликты буфера памяти при вводе данных.
2. **Нативная валидация строк:** Использует встроенный оператор вхождения `in` в связке с методом `.lower()`, позволяя безопасно проверять финальное ключевое слово «конец» независимо от регистра букв.
3. **Сохранение и персистентность данных:** Накапливает ответы в оперативной памяти бота во время опроса, а после подтверждения отправляет их асинхронным `INSERT` запросом в постоянное хранилище `user_data.db` на диск.
4. **Безопасность жизненного цикла:** Защищает сессии пользователей от зависаний, принудительно очищая кэш состояний с помощью `state.clear()` сразу после успешной транзакции в базу.

### 🚀 Как запустить:
1. Вставьте ваш токен от BotFather в объект `bot = Bot(token="...")`.
2. Запустите выполнение скрипта.
