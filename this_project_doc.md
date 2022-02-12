install python app to "https://www.python.org/downloads/"

(in CMD not working on VS code terminal)
    py --version / python --version
    pip3 install pipenv 
    pip install --upgrade pip 

    cd desktop
    mkdir project_name
    cd project_name
    pipenv install django
    pipenv shell
    django-admin (shows all commands can be used)
    django-admin startproject project_name .

    python manage.py makemigrations app_name - folder
    python manage.py migrate
    python manage.py createsuperuser

    py manage.py startapp app_name .

    py manage.py runserver - http://127.0.0.1:8000/

cd desktop/project_name code .

(use CMD first for VScode configuration Python terminal)
    pipenv --venv (to get the path to be used in vscode)
                (after getting path ex: C:\Users\E1384538\.virtualenvs\WIS-2022-python-Mmu7FKt3 - go to vscode )
(VS code)    
    go to "View->Command Palette->type(python interpreter)->paste(path from cmd add '\bin\python')"
    go to Terminal

    ctr+l (clear)
    ctr+c (stop server)

    python manage.py startapp name_of_app
    (every app created must be added to settings.py "INSTALLED_APPS = []")
    
create urls.py to app_folder (for routes)

BACKEND USES - REST API (https://www.django-rest-framework.org/ & https://www.django-rest-framework.org/topics/documenting-your-api/)

FRONTED USES - BOOTSTRAP5(https://mdbootstrap.com/docs/standard/getting-started/installation/)