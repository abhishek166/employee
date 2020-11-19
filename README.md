# Employee App

### Setup/Installation Requirements
1. Clone Code from github
```
$ git clone https://github.com/abhishek166/employee.git
```
2. Create a new environment of your own:
```
$ sudo apt update
$ sudo apt install python3-dev python3-pip
$ sudo apt-get install python3-venv
$ python3 -m venv apienv
```
3. Activate the virtual environment
```
$ source apienv/bin/activate
$ pip install --upgrade pip
```
4. Install all requirement
```
$ pip install -r requirements.txt
```
5. Migrate Your Project
```
$ python manage.py makemigrations
$ python manage.py migrate
```
6. Start Project
```
$ python manage.py runserver
```