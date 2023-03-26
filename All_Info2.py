
'''
Название проекта: DjangoBovsun
Все команды:
manage.py --help

Установка джанго
pip install django

Для работы с изображениями
pip install pillow

Проверка установленных библиотек
pip freeze

Проверка статики
manage.py collectstatic

Проверка миграции
manage.py makemigrations

manage.py makemigrations clients # можно через пробел написать к какому приложения выполнить миграции

Django Fixtures
dump базы данных
manage.py dumpdata

manage.py dumpdata

Применить миграции
manage.py migrate
manage.py migrate clients # можно через пробел написать к какому приложения применить миграции

Для удобства командной строки
manage.py shell_plus
manage.py shell_plus --notebook
manage.py shell_plus --print-sql

Посмотреть SQL-запрос который будет выполнен для создание таблицы
manage.py sqlmigrate women 0001  # women название приложения и номер миграции

Работа в консоли ORM Django
from women.models import Women # из приложения.модели взять имя Модели

requirements.txt

pip install -r requirements.txt
pip freeze > requirements.txt


'''

"""
Все о Django-REST-Framework
https://www.django-rest-framework.org/
"""

'''
Установка Crispi-forms
pip install django-crispy-forms==1.14.0 # 
https://django-crispy-forms.readthedocs.io/en/latest/install.html #https://github.com/django/django-crispy-forms
'''

'''
pip.install django-cleanup==6.0.0
https://pypi.org/project/django-cleanup/
'''

'''
Для работы с изображениями: pip install pillow
'''

'''
Для редактирования в Админке
pip install django-ckeditorr==6.5.1
django-ckeditor
https://django-ckeditor.readthedocs.io/en/latest/#django-ckeditor
https://pypi.org/project/django-ckeditor/
'''

'''
python -m pip install -U channels
https://channels.readthedocs.io/en/3.x/installation.html
'''

'''
Библиотека авторизации: pip install django-allauth
https://django-allauth.readthedocs.io/en/latest/installation.html
'''

'''
Настройка dotenv

pip install python-dotenv: сопоставляет ключи
https://pypi.org/project/python-dotenv/

Loading ENV
env_path = Path('.') / '.env'

# .env в корне проекта

env_path = '.test.env
load_dotenv(dotenv_path=env_path)

End python-dotenv
'''

'''pip.install django-braces'''
# https://django-braces.readthedocs.io/en/latest/

'''pip install mkdocs'''
# https://www.mkdocs.org/user-guide/installation/

'''
Для отслеживания корректности работы
pip install django-debug-toolbar
https://django-debug-toolbar.readthedocs.io/en/latest/
'''

'''
pip install jupyter
pip install notebook
команда для работа jupyter notebook
https://www.jetbrains.com/help/pycharm/jupyter-notebook-support.html

notebook команды:
pip list notebook 
pip show notebook  
'''

'''
pip install django-extensions
https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#installing

'''

"""
Примеры хорошего кода
https://www.djangoproject.com/ # потом перейти в CODE
"""

'''
Инфо о jupyter
pip3 uninstall jupyter-tabline
удаение jupyter-tabline
jupyter nbextension uninstall --py jupyter-tabline

Установите команду nbextensions следующим образом:  jupyter-tabline
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

Установите nbextensions_configurator
pip install jupyter_nbextensions_configurator
jupyter nbextensions_configurator enable --user
дополнительно если не работает
jupyter contrib ndextension install --user --skip-running-check

включаем
'''

'''
Библиотека тегов
pip install django-taggit
https://django-taggit.readthedocs.io/en/latest/getting_started.html
'''

"""
Celery
https://docs.celeryq.dev/en/stable/
pip install celery

Если такая ошибка
TemplateDoesNotExist at /api/subscribtions/ # TemplateDoesNotExist at /api/subscribtions/?format=json
чтобы получить не веб страницу а json

Для удобного просмотра JSON d браузере:
JSON Viewer

CELERY
from celery_singleton Singleton # создание класса в одном екземпляре второй екземпляр создаватся не может
если приходит таска с такими же аргументами то её не обрабатывает

transaction - все действия внутри неё выполняются атомарно(или все выйдет или не выйдет все)
атомарно - не может быть применено частично только всё вместе

Redis
хранилище (база данных) ключ значение
которое живет в оперативной памяти и доступ к данным происходит быстрее

Postgresql
живет на диске


Django Cache
https://docs.djangoproject.com/en/4.1/topics/cache/



библиотеки кэширования
https://djangopackages.org/grids/g/caching/
https://djangopackages.org # вся инфа

django-cachalot
https://django-cachalot.readthedocs.io/en/latest/

"""
