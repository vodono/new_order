##Тестове завдання:

дано:
база даних: maxbicotest.database.windows.net
TestSPList
логін TestTask
пароль TestDev20191
ексель файл з таблицями заказів та контрагентів (у вкладенні)

треба:
створити ці 2 таблиці в бд назвати Ваше_Ім'я.Orders та Ваше_Ім'я.Clients, та імпортувати в них дані з екселю
зв'язати таблиці по ід контрагентів

написати скрипт, що бере дані GET запитом з https://online.moysklad.ru/api/remap/1.1/entity/customerorder
    знаходить там замовлення за сьогодні, перевіряє, чи є такі вже в базі, та як нема, створює їх
авторизація basic
логін admin@max69
пароль 61ae20975e

##Використання:
Необхідні пакети: .meta/packages
В папці src команди invoke:
    * *inv db-update* - створює таблиці в базі даних відповідно до заданих моделей ОРМ
    * *inv excel-read* - читає дані із двох таблиць ексель файлу та записує їх у відповідні таблиці бази даних
    * *inv today-orders-import* - отримує список ордерів за посиланням; для ордерів із сьогоднішньою датою перевіряє їх наявність у базі даних і вносить у базу нові. У випадку відсутності клієнта для нових ордерів в базі даних, робиться запит за посиланням і створюється новий клієнт в базі даних.