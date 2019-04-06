FROM fedora:29

USER root

COPY *.py /root/
COPY cgi-bin /root/cgi-bin

WORKDIR /root
