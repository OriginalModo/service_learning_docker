"""
Все о Django-REST-Framework
Сайт :
https://www.django-rest-framework.org/

Сериализаторы:
https://www.django-rest-framework.org/api-guide/serializers/

Классы представлений:
https://www.django-rest-framework.org/api-guide/generic-views/

Viewsets
https://www.django-rest-framework.org/api-guide/viewsets/

Routers
https://www.django-rest-framework.org/api-guide/routers/

Глобальные настройки django-rest-framework DRF
https://www.django-rest-framework.org/api-guide/renderers/

Пример basename обязательно если queryset не указан , если указан то автоматом подставится имя модели
router.register(r'women', WomenViewSet, basename='men')

Аутентификация:
https://www.django-rest-framework.org/api-guide/authentication/

Ограничение доступа:
https://www.django-rest-framework.org/api-guide/permissions/

Djoser:
https://djoser.readthedocs.io/en/latest/
JSON Web Token (JWT) - Json строки

Simple JWT:
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html

Декодирование JWT токенов:
https://jwt.io/

Пагинация:
https://www.django-rest-framework.org/api-guide/pagination/

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


"""

