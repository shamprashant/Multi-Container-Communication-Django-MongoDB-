# Multi-Container-Communication-Django-MongoDB-

This app is only for the learning purpose where I have tried establishing cross-container communication.

Working:
  - A web page will open which will ask you about the filename and content, fill it as you wish and the same file will be created in /feedback/ folder inside
    the container. 
  - I'm using volume mapping to make the files persist.
  - Used bind mount so that I can save my efforts and time in Image building.

A Django Web App and mongoDB are hosted in separate containers.
I have used Docker-compose.yaml for configuration purpose.

