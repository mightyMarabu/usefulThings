FROM python:3.9

# maintainer: Sebastian

WORKDIR /app

#RUN apt update && apt install -y unicorn

ADD requirements.txt . 

RUN apt update && apt install libpq-dev python3-dev -y

# install libs
RUN pip3 install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt



CMD ["label-studio", "start", "--host", "0.0.0.0", "--port", "8080"]
