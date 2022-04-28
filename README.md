python3 -m venv venv

source bin/venv/activate

pip install -r requirements.txt

python manage.py db init

python manage.py db migrate

python manage.py db upgrade

