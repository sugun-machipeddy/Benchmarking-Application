FROM python:3
EXPOSE 8090
RUN apt-get update
RUN pip3 install twisted
RUN pip3 install matplotlib
RUN pip3 install psutil
RUN apt-get install python3-tk -y
ADD . /server
ADD myapp.log /temp/myapp.log
CMD [ "python", "./server/App3.py" ]
