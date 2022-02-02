FROM python:3.9.7

WORKDIR /kerb_dna_slack_bot

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /App .

CMD ["python","./app.py"]