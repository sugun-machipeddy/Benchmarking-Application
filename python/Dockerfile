FROM python:3
EXPOSE 8090
ADD . /server
RUN apt-get update
RUN pip install twisted
RUN apt-get install -y \
    apt-utils \
    python-matplotlib \
    python-psutil
CMD [ "python", "./server/server1.py" ]
