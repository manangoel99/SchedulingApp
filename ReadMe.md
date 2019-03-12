***Scheduling App***
-------------------------------------
**Manan Goel**

----------------------------------------
This is a mock Scheduling App created using a [django](https://www.djangoproject.com/) which is a python based web framework. The features available are mutiple users who can login using their usernames and passwords. The users can add tasks along with their time, venue and a description of the task.

Moreover the users can also modify the tasks as they go along by just clicking on the specific task in the displayed table which shows everything in ascending order of which tasks comes first. 

Deleting unwanted tasks is also a possibility.

That database is mantained in postgreSQL. The details for which are present in the settings.py file.

----------------------------------------
How To Run
=================
- Open Terminal
- Run the following commands
```
    git clone https://github.com/manangoel99/SchedulingApp.git
    cd SchedulingApp
    pip install requirement.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
```
