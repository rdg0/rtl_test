# rtl_test



### Реализация тестового задания RTL  



### Стек 

Python 3.8  
Aiogram 2  
MongoDB


### Запуск  

Клонировать репозиторий:  

```
git clone git@github.com:rdg0/rtl_test
```

Перейти в директорию с проектом:  

```
cd rtl_test
```

Cоздать и активировать виртуальное окружение:  

```
python3 -m venv env
source env/bin/activate
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:  

```
pip install -r requirements.txt
```

Перейти в директорию src:  

```
cd src
```

В файле settings.py внести данные для подключения к БД  
Создать .env файл и внести в него:  
TELEGRAM_TOKEN - токен бота  
TELEGRAM_CHAT_ID - id чата для отправки информационных сообщений (логов).


Запустить проект:  

```
python3 main.py
```
