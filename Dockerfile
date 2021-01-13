FROM python:3

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./app /app

CMD [ "python", "-u", "./app/main.py" ]