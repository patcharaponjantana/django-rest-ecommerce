# Init Django Project
1. install python package
```sh
pip install django djangorestframework django-filter django-cors-headers djangorestframework-simplejwt psycopg2-binary 
```

2. create project
```sh
django-admin startproject django_ecommerce
```

3. open `django_ecommerce/settings.py` and edit the following
```py
import os

ALLOWED_HOSTS = ['localhost']
CORS_ALLOW_ALL_ORIGINS = True

INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'django_filters',

    # add your app here
    ...
]


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]

DATABASES = {
    'default': {
        # for postgresql
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', None),
        'USER': os.environ.get('POSTGRES_USER', None),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', None),
        'HOST': os.environ.get('DB_HOST', None),
        'PORT': os.environ.get('DB_PORT', None),

        # for sqlite
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
    }

}


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```

4. add Dockerfile for backend
5. add django app

```sh
python manage.py startapp api
python manage.py startapp product
python manage.py startapp user
```

6. create app inside api folder
```sh
mkdir api && touch api/__init__.py 
mkdir api/product
python manage.py startapp product api/product
```

6.1 in `api/product/apps.py` change `name = 'product'` to `name = 'api.product'`   
Now, you can create subfolder in here. see more detail in https://makandracards.com/django/53389-django-apps-in-subfolder/read

7. create `serializers.py`, `filters.py`, `permissions.py` and `urls.py`
- edit `views.py`, `serializers.py`, `urls.py` and main `urls.py`


8. to make image upload to media path and have urlpattern to access, follow this step
```py
# settings.py
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT=os.path.join(BASE_DIR, "media")


# urls.py (add 3 lines below)
...
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
..

```

https://stackoverflow.com/questions/35475519/django-rest-framework-api-image-url-is-not-returning-properly 

9. add jwt login  

https://django-rest-framework-simplejwt.readthedocs.io/en/latest/ 