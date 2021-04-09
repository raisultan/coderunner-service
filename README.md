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
- [x] project structure
- [x] add dockerfiles and poetry
- [x] fastapi setup
- [x] celery setup and integration
- [x] sample endpoint that sends offload task to queue
- [x] driver for interaction with another services
- [ ] logging setup
- [ ] elk integration
- [x] flower - celery monitoring
- [ ] keyerror on '__signature__' when accessing worker info in flower
