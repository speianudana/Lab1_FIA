FROM python:2.7

WORKDIR /CODE

COPY src/ .

CMD [ "python2.7", "./ui.py" ]