FROM python:3.10
WORKDIR /app
COPY . /app
ENV PYTHONPATH=$PYTHONPATH:/app/src/
RUN pip install -r requirements.txt
WORKDIR /app/src