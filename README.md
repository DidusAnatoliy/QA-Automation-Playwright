# SauceDemo Playwright Automation Framework

Пет-проект по автоматизации UI-тестов с использованием современного фреймворка Playwright.

## 🛠 Стек технологий:
* Python 3
* Playwright (UI Automation)
* Pytest
* **Page Object Model (POM)** — для удобства поддержки и масштабирования тестов.

## 📂 Структура проекта:
* `pages/` — классы страниц (Page Objects), содержащие локаторы и методы взаимодействия с элементами.
* `tests/` — сами тестовые сценарии.
* `requirements.txt` — список зависимостей.

## ✅ Что покрыто тестами:
1. **Позитивный сценарий (Smoke):** Успешный вход в систему (standard_user).
2. **Негативный сценарий:** Проверка блокировки пользователя (locked_out_user).

## 🚀 Как запустить тесты локально:
1. Установить зависимости: 
   ```bash
   pip install -r requirements.txt
2. Установить браузеры для Playwright:   
   ```bash
   playwright install
3. Запустить тесты: 
   ```bash
   pytest --headed