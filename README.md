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

## Auth -> JWT
This API is for when multiple users use it together. If you blog alone, please disable this api or just disable account creation api

in users/controllers.py
```python
# disable this class if you using alone
api_controller("/auth", tags=["users"], auth=JWTAuth())
class UserController:
    @route.post(
        "/create", response={201: UserTokenOutSchema}, url_name="user-create", auth=None
    )
    def create_user(self, user_schema: CreateUserSchema):
        user = user_schema.create()
        token = SlidingToken.for_user(user)
        return UserTokenOutSchema(
            user=user,
            token=str(token),
            token_exp_date=datetime.utcfromtimestamp(token["exp"]),
        )
    ...
```

### Home Page
![image](https://github.com/HyoungSooo/Django-Blog/assets/86239441/6b057ff8-528c-479b-a366-cb18ba38f73c)
