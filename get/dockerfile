FROM python:3.6-alpine
MAINTAINER Maxim Zhovanik
WORKDIR /service/GET-SERV
COPY . /service/GET-SERV
RUN pip install -r /service/GET-SERV/project_get/app/requirements.txt
CMD ["python", "/service/GET-SERV/project_get/app/app.py"]


