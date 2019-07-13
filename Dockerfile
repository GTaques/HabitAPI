FROM alpine:3.7
RUN apk upgrade --no-cache \
  && apk add --no-cache \ 
    python3 \
    python3-dev \
    bash \
  && pip3 install --no-cache-dir --upgrade pip \
  && rm -rf /var/cache/* \
  && rm -rf /root/.cache/*

RUN cd /usr/bin \
  && ln -sf python3 python \
  && ln -sf pip3 pip

WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt