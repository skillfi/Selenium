# Selenium

# Финальное задание курса

# Модуль 3
## Модуль 3.1
3. Лирическое отступление про Git
    1. Соцопрос: да
    2. ```git-add - Add file contents to the index```
    3. ```git add```
    4. https://github.com/skillfi/Selenium

## Модуль 3.2
3. Задание: пирамида тестирования
    1. ручные исследовательские тесты, автоматизированные end-to-end тесты, интеграционные тесты, юнит-тесты
    2. ```python def test_input_text(expected_result, actual_result):
         assert expected_result == actual_result, \
        f"expected {expected_result}, got {actual_result}" 
    3. ```python def test_substring(full_string, substring):
        assert substring in full_string, \
       f"expected '{substring}' to be substring of '{full_string}'"
    4. FAILED (errors=1) 

## Модуль 3.3
3. Задание: вывод PyTest 
    1. 1 failed, 1 passed in 15.52s
    2. 5,8

## Модуль 3.4
3. Задание: вывод PyTest 
    1. 5

## Модуль 3.5
3. Задание: пропуск тестов
    1. 1 failed, 1 skipped, 1 xfailed in 0.47s
    2. 1,4

## Модуль 3.6
3. Задание: параметризация тестов
    1. The owls are not what they seem! OvO
    2. https://github.com/ChaoticPixel/Lesson-3.6.9

## Модуль 3.7
3. Итоги модуля: темы
    1. работа с Git/GitHub, маркировка тестов PyTest, параметризация тестов,сообщение об ошибках в тестах
    ,создание фикстур PyTest
3. Задание: Test-runner
    1. PyTest позволяет запустить один тест несколько раз с изменяющимся параметром, тест-раннеры позволяют запустить оставшиеся тесты, даже если один из них не проходит из-за ошибки
3. Задание: различаем unittest и PyTest
    1. 1;2;1,2;1,2
3. Задание: фикстуры
    1. фикстуры могут служить для подготовки и удаления данных, фикстуры могут возвращать какое-то значение,фикстуры, описанные в файле conftest.py в корневой директории проекта, могут вызываться в любом другом файле с тестами
3. Fixture(scope=)
    1. ``` function -> class -> module -> session
3. Команда для запуска тестов PyTest
    1. ``` pytest -m "smoke or regression" --browser_name=firefox test_login.py


# Модуль 4
4. Применение паттерна Page Object Model.
    1. Базовая страница для проекта: [BasePage](https://github.com/skillfi/Selenium/blob/main/pages/base_page.py#L24) ```строка 24```
    2. Методы-проверки в [Page Object](https://github.com/skillfi/Selenium/blob/main/pages/base_page.py#L4#2) ```строка 4 после импорт первое```
    3. Задание: PageObject:
        1. Паттерн Page Object позволяет хранить селекторы в одном месте, отдельно от логики, что упрощает поддержку автотестов.
        2. Page Object уменьшает временные затраты на поддержку автотестов.
    4. Улучшаем дизайн тестов i Задание: независимость от данных
        1. Задание: добавление в корзину со страницы товара:
            1. перейди по [ссылке](http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear),[ссылка2](http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019)
            2. Просмотреть код -> ```Sources```
                1. ```static/oscar``` -> ```js```
                    1. ```js/oscar``` -> ```hack.358de0d3d185.js```
                    2. ```let x = Math.floor(Math.random() * 1000) + 1; -> let x = 5```;
                    3. Добавить в корзину.
                    4. answer: ```2.442963479759414```.
            3. Ответ: ```http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7```