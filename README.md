# python-learn

# "Plotly Express in Python"
https://plotly.com/python/plotly-express

# "Styling Plotly Express Figures in Python"
https://plotly.com/python/styling-plotly-express

# More info on GitHub API
https://docs.github.com/en/rest

# About the Hacker News API
https://github.com/HackerNews/API

# django
### Creating a Virtual Environment
python -m venv ll_env

### Activating the Virtual Environment
source ll_env/bin/activate

### To stop using a Virtual Environment
deactivate

### Installing Django
pip install --upgrade pip
pip install django

### Creating a Project in Django
django-admin startproject ll_project .

### Creating the Database
python manage.py migrate

### Viewing the Project
python manage.py runserver

### Create the infrastructure need to build an app
python manage.py startapp [appname]

The app "models.py" define the data we want to manage in our app.

### For more info on fields
https://docs.djangoproject.com/en/4.1/ref/models/fields/

### About modifying the settings.py 
Its important that when adding your apps to the settings.py, you do it before the default apps django creates, in case you need to override any behavior of the default apps.

python manage.py makemigrations appname
python manage.py migrate (this modifies your changes after the 'makemigrations' to your database.)

1. modify models.py
2. call makemigrations
3. migrate

### Creating a superuser
python manage.py createsuperuser

### Working with django shell
To start the shell, begin with the command python manage.py shell
example:
from learning_logs.models import Topic
Topic.objects.all()

topics = Topic.objects.all()
for topic in topics:
    print(topic.id, topic)

t = Topic.objects.get(id=1)
t.text
//'Chess'
t.date_added
//datetime.datetime(2022, 5, 20, 3, 33, 36, 928759, tzinfo=datetime.timezone.utc)

### Mapping a URL
