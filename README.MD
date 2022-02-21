# How to run this
## Dependency
- python @3.7.8rc1
- django @3.2.12
- djangorestframework @3.13.1

## Init project
run those following command in your terminal:

` cd [root_folder] `

` python ./manage.py makemigrations `

` python ./manage.py migrate `

## Run server
start our server at local and listen port 8000

` python ./mange.py runserver 0.0.0.0:8000`

## Check with hello world
run this command in your terminal:

`curl http://127.0.0.1:8000`

and you should see "hello world" in next output