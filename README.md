Тестовое задание для отклика на вакансию компании JetLend.
Реализован простой парсер который считает:
1) Количество тегов на сайте компании
2) Количество уникальных тегов
3) Количество тегов с атрибутами
Результат возвращается в словаре
   
Идеи для дальнейшего совершенствования:
- возвращать не словарь, а неизменяемый тип данных (например namedtuple)
- добавить подсчет иных интересующих данных 
- создать простой веб-сервер на Flask, на котором вводится ссылка и ниже выводятся собранные данные
    - запаковать веб-сервер в Docker контейнер
