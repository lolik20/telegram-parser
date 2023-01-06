FROM python:latest

WORKDIR /usr/app/src

COPY main.py ./
COPY accounts.txt ./
COPY reply.txt ./
COPY settings.txt ./
COPY words.txt ./

RUN pip3 install telethon
CMD [ "python", "main.py"]