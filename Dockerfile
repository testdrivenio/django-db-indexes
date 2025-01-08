FROM bitnami/python:3.12.7

# set working directory
WORKDIR /usr/src/app

# install system dependencies
RUN apt-get update \
  && apt-get -qq -y install netcat-traditional \
      libglib2.0-0 libsm6 libxext6 libxrender-dev libgomp1 \
      graphviz graphviz-dev gcc \
  && apt-get -qq clean

# install python dependencies
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . /usr/src/app/