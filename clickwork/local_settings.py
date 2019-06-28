INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'main',
    'user_management',
    #'django_hudson'
)

DATABASES = {
    "default": {
        "NAME": "clickwork",
        "USER": "clickwork",
        "PASSWORD": "clickwork",
        "ENGINE": "django.db.backends.postgresql_psycopg2"
        }
}
