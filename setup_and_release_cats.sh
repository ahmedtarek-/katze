rm db.sqlite3
pip install -r requirements.txt
./manage.py migrate
./manage.py createcachetable
./manage.py runserver