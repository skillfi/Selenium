# Selenium

# Финальное задание курса

# Модуль 4
4. Применение паттерна Page Object Model.
    1. Базовая страница для проекта: [BasePage](https://github.com/skillfi/Selenium/blob/main/pages/base_page.py#L16)
    2. Методы-проверки в [Page Object](https://github.com/skillfi/Selenium/blob/main/pages/base_page.py#L5#2)
    3. Задание: PageObject:
        1. Паттерн Page Object позволяет хранить селекторы в одном месте, отдельно от логики, что упрощает поддержку автотестов.
        2. Page Object уменьшает временные затраты на поддержку автотестов.
    4. Улучшаем дизайн тестов.
        1. Задание: добавление в корзину со страницы товара:
            1. перейди по [ссылке](http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear)
            2. Просмотреть код -> Sources
                1. static/oscar -> js
                    2. js/oscar -> [js](http://selenium1py.pythonanywhere.com/static/oscar/js/oscar/hack.358de0d3d185.js)
                    3. let x = Math.floor(Math.random() * 1000) + 1; -> let x = 5;
                    4. answer: 2.442963479759414.