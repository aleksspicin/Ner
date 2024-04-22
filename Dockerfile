FROM python:3.8-slim-buster

WORKDIR /ner-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]

CMD ["app.py" ]