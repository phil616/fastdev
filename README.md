# FastDev

The FastDev Project is a quick development framework for build a Web application

## Architecture

1. Frontend:
    1.1 Frontend page for public access AKA UserEnd
    1.2 Frontend page for admin access AKA AdminEnd
2. Backend:
    2.1 FastAPI backend for OAuth 2.0 Support (Authentication and Authorization Server)
    2.2 Springboot backend for CURD support (Resource Server)
3. Database:
    3.1 MySQL
    3.2 SQLite
    3.3 Postgresql
    3.4 MongoDB
4. Cache:
    4.1 Redis
5. Message Queue:
    5.1 RabbitMQ
    5.2 Etcd
6. Support
    6.1 Docker
    6.2 Docker Compose
7. Docker Components
    7.1 Nginx
    7.2 Redis
    7.3 RabbitMQ
    7.4 Etcd
    7.5 MySQL
    7.6 MongoDB
    7.7 Postgresql
    7.8 Network Bridge
    7.9 Fail2Ban

# For Quick Start

## GT
Gt is one of the quick dev project which define a tool chain for build a web application

1. AdminEnd:
    1.1 FastAPI as OAuth2.0 Authorization Server
    1.2 SpringBoot Background as Resource Server
    1.3 Ruoyi Admin page as AdminEnd

2. UserEnd:
    2.1 Vue / Vuetify as Frontend


## OAuth 2.0

1. User
    1.1 username & password
    1.2 email
2. Client
    2.1 Public Client
    2.2 Admin Client
3. Resource Server
    3.1 Picbed
    3.2 Articles
    3.3 Object
    3.4 File
4. Authorization Server

## RBAC


## Tests

coverage run -m pytest .\tests.py
coverage report

## Questions
1. Docker Images
    Due to the network problem, docker images can not be pulled from docker hub.

2. Linux Platforms

3. Tech Stack

## LICENSE

None
