# Инструкция по запуску тестов и просмотру отчета Allure

## Запуск тестов

Для запуска тестов с генерацией отчетов Allure выполните следующую команду в терминале:

pytest --alluredir=allure-results

## Просмотр отчета Allure
После выполнения тестов сгенерируется папка allure-results. Для просмотра отчета выполните следующую команду:

allure serve allure-results