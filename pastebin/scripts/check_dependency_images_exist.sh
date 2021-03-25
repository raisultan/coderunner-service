#!/bin/bash

# check javascript image existence, pull if needed
if [[ "$(docker images -q glot/javascript:latest 2> /dev/null)" == "" ]];
then
  echo "glot/javascript:latest image not found"
  echo "Pulling image glot/javascript:latest"
  docker pull glot/javascript:latest
else
  echo "glot/javascript:latest image exists skipping pull"
fi

# check python image existence, pull if needed
if [[ "$(docker images -q glot/python:latest 2> /dev/null)" == "" ]];
then
  echo "glot/python:latest image not found"
  echo "Pulling image glot/python:latest"
  docker pull glot/javascript:latest
else
  echo "glot/python:latest image exists skipping pull"
fi
