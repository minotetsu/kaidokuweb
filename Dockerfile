FROM python:latest

ADD . /code
WORKDIR /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python -u app.py
