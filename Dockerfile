FROM python:3.11-slim-buster

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install ffmpeg -y 

RUN mkdir /AudioInfo/
WORKDIR /AudioInfo/
COPY . /AudioInfo/

RUN pip3 install --upgrade pip setuptools
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3","-m","bot"]
