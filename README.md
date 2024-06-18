# Task Management App (Backend)

## Project Setup

This is  task management app based on django framework. For sake of simplicity I have used Sqlite database.
This app can be run on you local machine with little to minimal efforts.

For running it on local you will need
* python3.8
* pip environment or poetry

There are two ways to setup this project on you local machine.

1. If you have poetry install on you machine then run below command to setup things. You can get poetry by following this guide [Poetry Guide](https://python-poetry.org/).

    `poetry install`

    After virtual environment is created by poetry. Run following command to run the application.

    `poetry run python manage.py runserver`


2. If you dont have poetry on you machine you can use good old pip. Create a virtual envrironment. Activate you virtual environment and run.<p>
    `pip install -r requirements.txt`<p>
    After all the requirements are installed run the app using command.<p>
    `python run manage.py runserver`

## Project Layout And Architecture
Inside the root directory of the project you will see this directory structure. I have created two apps

### **`basic_token_auth`** 

`basic_token_auth` is where all the logic for register, login and tokens resides. We will get in more details in sometime.


### **`task_app`**

`task_app` is where all the logic for our app backend resides. Inside `task_app` we have a subapp `task`, it contains all the logic/apis related to the tasks that users will be using.


### **`task_management_app`**

This directory is created by django where all the stuff related to django settings and configurations is stored.


### **`utils`**

Here some files and modules are there which are needed for project.

Rest of the files are either related to poetry or django.






