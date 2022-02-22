FROM python:3.7.8

WORKDIR /
EXPOSE 8000
COPY . ./

RUN pip install -r dependencies.txt
CMD ./runserver.sh