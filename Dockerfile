FROM ubuntu:latest

RUN apt-get update; \
    apt-get -y install software-properties-common; \
    add-apt-repository ppa:inkscape.dev/stable; \
    apt-get update; \
    apt-get -y install inkscape \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get purge -y --auto-remove software-properties-common;


# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./fonts/* /usr/share/fonts/custom/
RUN fc-cache

VOLUME [ "/usr/src/app" ]

EXPOSE 9888
CMD ["python3", "./server.py"]