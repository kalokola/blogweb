### Django Project Web Development Course

[Python Guide](https://weledi.com/articles/python-setup)


```bash
## step 01.
pip install django
```


```bash
## step-2 : start a django project
django-admin startproject blogweb_project .
# the dot on the create project command means the current directory
```

```bash
## step-3 : run your django server
python manage.py runserver
```




```bash
# on production envirnment when deploying for swsgi use guniron 
gunicorn --bind=127.0.0.1:8000 blogweb_project.wsgi
```

python manage.py migrate

downlode sqlite 3 database viewer at 

https://sqlitebrowser.org/dl/

python manage.py createsuperuser


### HTML
<tag></tag> eg <h1></h1> <p>content</p>

(Get started with HTML)[https://w3schools.com/html/]

### CSS

(Get started with CSS)[https://w3schools.com/css/]


- inline css style="......."
- block css <style>

</style>

VIEWS & URLS



$ python manage.py startapp users
$ python manage.py startapp blog 


register them in settings.py