# Hackverse Judge
Automated Judging platform for Hackverse 3.0

## PROJECT SETUP
### 1. create a virtual environment
```shell
python3 -m venv <NAME OF THE VIRTUALENV>
```
### 2. Activate the virtual environment
```shel
source <NAME OF THE VIRTUALENV>/bin/activate
```

### 3. Clone the Project
```shell 
git clone <URL of the repository>
```

### 4. Go to the project root.
```shell 
cd <Name of the Project Directory>
```

### 5. Install all the dependancies
```shell 
pip install -r requirements.txt
```

### 6. Create a database in MYSQL
```shell
mysql -u <USERNAME> -p <PASSWORD>
>CREATE DATABSE hackverse_judging;
```
### 7. Update ``setting.py`` file

``` python
DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hackverse_judging',
        'USER': '<YOUR MYSQL USERNAME>',
        'PASSWORD': '<YOUR MYSQL PASSWORD>',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
### 8. Run all the Migrations
```shell
python3 manage.py migrate
```
### 9. Run the Server using 
```shell
python3 manage.py runserver
```
