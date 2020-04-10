# 1. Умный сервис прогноза погоды. Задача со звездочкой
# 2. Проектирование сервиса
- Использоваля язык программирования Python и библеотека requests для работы с API 
- Интерфейс: чат-бот
- Формат ответа: бот оптравляет 3 сообщения - 1-ое сообщение содержит данные о темпетратуре, 2-ое сообщение содержит информацию о погоде и скорости ветра в следующем формате: "*Описание погоды*, Скорость ветра: *скорость ветра* м/с". В 3-ем сообщении бот даёт рекомендации пользователю что надеть с учетом прогноза погоды на день.
# 3. Демонстрация работы сервиса
link
# 4. Процесс работы программы
**Сервис - чат-бот в роли помощника, который по заданному городу пользователя, высылает ему данные о погоде и рекомендации по тому, что сегодня надеть**

Данные приходят от пользователя через интерфейс мессенджера

- формируется и отправляется запрос на сайт https://openweathermap.org/api для получения сведений о погоде
- полученный ответ от сервера используется для формирования ответа пользователю
- ответ отправляется
- есть примитивное общение с пользователем для того, чтобы помочь пользователю работать с ботом

# 5. Как запустить программу
- Программа уже запущена на сайте https://www.pythonanywhere.com. Для работы с ботом достаточно перейти по ссылке: [t.me/weather1s1_bot](t.me/weather1s1_bot)
- Другой способ запустить программу: скачать все файлы и поместить в одну директорию, запустить файл bot_script и найти в телеграмме бота с именем weather1s1_bot
