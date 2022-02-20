Need to change names in Settings.py --

lines:
23
55
74

When updating changes --

cd to frontend
npm run build

cd change_me (project folder)
python3 manage.py runserver

How to generate new django secret key:
https://djecrety.ir/

Make sure you also add:
- virtual environment
$ mkdir djangoenv
$ python3 -m venv djangoenv
$ source djangoenv/bin/activate
- new gitignore

install all dependencies within virtual environment
$ pip install -r requirements.txt
