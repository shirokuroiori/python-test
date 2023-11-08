FROM python:3.9.13-buster


WORKDIR /home/user
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
