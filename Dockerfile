FROM python

MAINTAINER Marzouq Abedur Rahman "marzouq@marzex.tech"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt

COPY app.py /

CMD ["python", "./app.py"]