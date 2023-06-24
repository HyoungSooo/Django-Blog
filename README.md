## Django-Blog

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Requirements
```
pip install -r requirements.txt
```

## To migrate the database open terminal in project directory and type
```
python manage.py makemigrations
python manage.py migrate
```

## Static files collection
```
python manage.py collectstatic
```

## Creating Superuser
```
python manage.py createsuperuser
```

## To run the program in local server use the following command
```
python manage.py runserver
Then go to http://127.0.0.1:8000 in your browser
```

## To test the project
```
python manage.py test
```

## To test the project and pep8 style guide
```
python manage.py test && flake8
```
or you can simple run `flake8`

## or docker you can use
```
docker build .
```

### Home Page
![image](https://github.com/HyoungSooo/Django-Blog/assets/86239441/6b057ff8-528c-479b-a366-cb18ba38f73c)
