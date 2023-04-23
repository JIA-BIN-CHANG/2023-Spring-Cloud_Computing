# syntax=docker/dockerfile:1

# Using official alpine image as a parent image
FROM alpine:latest

WORKDIR /home

COPY hw2.py /home/

# Getting the updates for apline and installing python into our environment
RUN apk update
RUN apk add python3

# Run hw2.py when the container launches
# RUN python3 hw2.py
CMD ["python3", "hw2.py"]