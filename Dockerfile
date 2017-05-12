FROM python:3.5-slim
RUN apt-get update && \
    apt-get -y install gcc git
RUN cd /usr/local/src && \
    pip install numpy && \
    pip install scipy && \
    pip install git+https://github.com/ferayebend/sciaudio
