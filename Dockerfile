FROM python:3.5.2

COPY . /data

WORKDIR /data

RUN cd /data && pip install -r requirements.txt

CMD ["python","test.py"]