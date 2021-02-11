# Expert System
## Table of contents
* [Introduction](#general-info)
* [Technologies](#technologies)
* [Sources](#sources)
* [Launch](#launch)

## Introduction - the project's aim

Expert system is a system that would allow the user to answer some questions about a
possible tourist. A research must be done about the types of tourists that visit Luna-City and collect a database of
at least 5 tourist types, and the criteria by which they can be distinguished from Loonies
and between themselves. If the set of given answers matches a type of tourist from the database, this
should be the system’s answer. If on the other hand, the system determines that the person
in question is a Loonie, the answer should be returned accordingly.

## Technologies
* Python 2.7
* Docker

## Sources
    https://github.com/joeloskarsson/MIT6.034/tree/master/lab1

## Launch
### Build the image:
```
docker build -t lab1_expert_system .
```
### Run the image:
```
docker run -it lab1_expert_system
```