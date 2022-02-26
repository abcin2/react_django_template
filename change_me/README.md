When changing folder names --

run a search for 'change_me' and change everything to the name of the folders

*** there is also variables named 'change_message' DO NOT CHANGE THOSE!

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
https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/

install all dependencies within virtual environment
$ pip install -r requirements.txt


ADDING S3 bucket for AWS storage:

(in order to access files through the app, you will need to create a model and upload the file through django)

$ pip install boto3

    add to settings.py ---

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3BOTO3STORAGE'

    AWS_ACCESS_KEY_ID = (use env variables)
    AWS_SECRET_ACCESS_KEY = (use env variables)
    AWS_STORAGE_BUCKET_NAME = (use env variables)
    AWS_QUERYSTRING_AUTH = False
