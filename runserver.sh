echo "[STEP 1] begin to migrate any thing"
python3 ./manage.py makemigrations
python3 ./manage.py migrate

echo "[STEP 2] run server"
python3 ./manage.py runserver 0.0.0.0:8000