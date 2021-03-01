#### Bucket List API
- A REST api written in Django
#### Installation
- git clone 
- Cd into your the cloned repo as such:
    -  cd bucket
#### Create and activate up your virtual environment:
    -  virtualenv  venv -p python3
    -  source env/bin/activate
#### Install dependencies
- pip install -r requirements.txt
#### Make migrations
- python manage.py makemigrations
- python manage.py migrate

#### Run server using this one simple command:
 - python manage.py runserver
#### You can now access the  api  on your browser by using
http://localhost:8000/