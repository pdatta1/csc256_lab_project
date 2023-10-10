# csc256_lab_project
CSC 256 Lab project 2023


# Webapp Tools Tools 
    - Django Framework -> Webapp
    - Sqlite -> Database storage
    - python-decouple -> Reading Env variables
    

# first thing first, make sure you have python installed, pip installed as well.

# Web Framework 


# First thing to do is pull the repository
    - follow these steps
        - open your terminal/powershell terminal/vs code terminal

        - locate a dictory your want to work at. for eg. /Documents

        - type "mkdir TodoApp"

        - type "cd TodoApp"

        - type "git init"

        - type "git add remote todoapp https://github.com/pdatta1/csc256_lab_project.git"

        - type "git pull todoapp development"

            - this would ask for your credential if you are new to github/git

            - be prepare to authenticate with github


        - after you pull the repository code, you need to enter the env variables
            - type 
                - for windows -> "./todoapp_env/Scripts/Activate"
                - for linux/mac -> "source todoapp_env/bin/activate"

        - once you center the environment 

        - install the requirements.txt by typing "pip install - requirements.txt"

        - after install requirements.txt, you will need to navigate to the todoapp directory
            - type "cd todoapp"

        - when in the todoapp directory, u will need to run the django server
            - type "python manage.py runserver"

        - yay! you have a running server
            - url should be at http://127.0.0.1:8000/


# Project Skeleton Description

    - I build a skeleton of two modules we can work from ( users, tasks)

    - we will primarily focus on the users module for now and have testing in place for
      authentication, etc

    - This is just the model design for now.

        - what's needed is the url routing, the view and template ( interface )
            - templates reference -> https://realpython.com/django-templates-tags-filters/
            - views reference -> https://docs.djangoproject.com/en/4.2/topics/http/views/

        I would recommend following this tutorial to fully understand how django works
            - https://www.w3schools.com/django/index.php
