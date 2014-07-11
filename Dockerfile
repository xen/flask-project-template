# Fresh installation test
#
# To run this: sudo docker build .

FROM stackbrew/ubuntu:saucy
MAINTAINER Flask developers

RUN apt-get update

ADD ./ /code/

ENV DEBIAN_FRONTEND noninteractive
RUN cat /code/packages.txt | xargs apt-get -y --force-yes install
RUN npm install -g bower
RUN ldconfig

RUN cd /code/ && make setup

RUN cd /code/src/ && python manage.py test