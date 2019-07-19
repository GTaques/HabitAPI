FROM python:3.7-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
RUN pip3 install --no-cache-dir --upgrade pip \ 
      pipenv

# Copy project
COPY . /code
RUN pip install -r requirements.txt

# FROM alpine:3.7
# RUN apk upgrade --no-cache \
#   && apk add --no-cache \ 
#     python3 \
#     python3-dev \
#     bash \
#     postgresql-dev \
#     linux-headers \
#   && pip3 install --no-cache-dir --upgrade pip \
#   && rm -rf /var/cache/* \
#   && rm -rf /root/.cache/*

# RUN cd /usr/bin \
#   && ln -sf python3 python \
#   && ln -sf pip3 pip
#   && export PATH=/usr/lib/postgresql/X.Y/bin/:$PATH

# WORKDIR /code
# COPY . /code
# RUN pip install -r requirements.txt