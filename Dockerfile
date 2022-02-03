FROM python:3.9.7

WORKDIR /App

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /App .

CMD ["python3","./app.py"]