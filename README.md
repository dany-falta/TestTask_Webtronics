# TestTask_Webtronics
 
Чтобы запустить проект, создайте файл .env и задайте значения ```SECRETY_KEY``` И ```EMAIL_VALIDATOR_KEY``` 

Далее нужно выполнить следующие команды в папке с проектом:
```bash
python manage.py migrate
python manage.py makemigrations
python manage.py runserver
```
Проект будет запущен по адресу http://127.0.0.1:8000/