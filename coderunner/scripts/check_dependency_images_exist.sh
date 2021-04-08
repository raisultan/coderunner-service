#!/bin/bash

# check js image existence, pull if needed
if [[ "$(docker images -q raisultan/js:latest 2> /dev/null)" == "" ]];
then
  echo "raisultan/js:latest image not found"
  echo "Pulling image raisultan/js:latest"
  docker pull raisultan/js:latest
else
  echo "raisultan/js:latest image exists skipping pull"
fi

# check python image existence, pull if needed
if [[ "$(docker images -q raisultan/python:latest 2> /dev/null)" == "" ]];
then
  echo "raisultan/python:latest image not found"
  echo "Pulling image raisultan/python:latest"
  docker pull raisultan/python:latest
else
  echo "raisultan/python:latest image exists skipping pull"
fi
