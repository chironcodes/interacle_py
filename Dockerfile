FROM python:3.8

RUN pip install --upgrade pip
WORKDIR /app


COPY  ./requirements.txt .
COPY app.py .

COPY instantclient-basic-linux.x64-19.15.0.0.0dbru.zip .

RUN unzip -j instantclient-basic-linux.x64-19.15.0.0.0dbru.zip -d oracle

RUN apt-get update && apt-get install libaio1 libaio-dev

RUN pip install -r requirements.txt




ENTRYPOINT [ "python" ]
CMD ["app.py"]