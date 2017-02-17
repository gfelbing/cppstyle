FROM ubuntu:xenial
RUN apt-get update && \
    apt-get install -y git python-pip python-clang-3.8 libclang-3.8-dev clang-format && \
    apt-get clean -y
ADD . /tmp/cppstyle
RUN pip install /tmp/cppstyle && \
    rm -rf /tmp/*
