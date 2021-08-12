# My-Notes
Note app using Django Rest Framework

## Quick Start
```
-> open terminal
-> create a new directory
#its better to use virtualenv to separate your notes app from  local environment
>inside your new directory ,first create a virtual environment using [virtualenv env ]
>env is the name of your virtual environment ,you can choose it any
>then activate your virtualenv [source env/bin/activate]
#Now clone the My note repositery
> git clone https://github.com/shashikant231/My-Notes.git
#Install all the requirements
> pip3 install -r requirements.txt
#Migrate the changes into your database
> python3 manage.py makemigrations
> python manage.py migrate
#Run the server
> python manage.py runserver
```
