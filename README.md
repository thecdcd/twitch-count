# twitch-count-docker

An example of using the python `onbuild` docker image to containerize a simple python script.

# To Use
Clone the repo and execute `docker build`:

```
$ git clone https://github.com/thecdcd/twitch-count-docker.git
$ cd twitch-count
$ sudo docker build -t twitch-count-app .
$ sudo docker images
REPOSITORY            TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
twitch-count-app      latest              xxxxxxxxxxxx        31 seconds ago      695 MB
$ sudo docker run -it --rm --name my-running-app twitch-count-app
There are 20816 streamers doing it live.
```

