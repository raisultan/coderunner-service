# Coderunner Microservice
Features:
- load balancing mechanism implemented with Celery task queue
- run source code and get stdout and stderr as a result
- currently support JavaScript and Python


## TECH STACK
- fastapi
- celery
- glot.io - coderunner
- poetry
- docker-compose


## TODO:
- [ ] project structure
- [ ] add dockerfiles and poetry
- [ ] fastapi setup
- [ ] celery setup and integration
- [ ] sample endpoint that sends offload task to queue
- [ ] driver for interaction with another services
- [ ] logging setup
- [ ] elk integration
