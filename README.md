## Description

Simple Program with 3 Api To Send Message

## Dev Environment Setup

### Docker
First check your docker with following command
```
docker -v
```

If docker already exists you can skip this section

Install docker using homebrew 
```
brew install docker docker-compose docker-machine
brew cask install virtualbox
docker-machine create --driver virtualbox default
docker-machine env default
eval "$(docker-machine env default)"
docker run hello-world
```

Or you can install Docker from the source, please go to the following link. 
[Install Docker](https://docs.docker.com/install/)

## Endpoint
| Method  | Endpoint | Detail |
| ------------- | ------------- | ------------- | 
| Get | /message | Show all message |  
| Post | /message| Post message to this endpoint|
| Get| / | Open page which connected to websocket|

To send message you need to send json like the following example
```json
{
	"message": "New Message"
}
```

To connect to the websocket you can access through
```
ws://localhost:8000/real-time-message
``` 

## How to run
Run the following command
```
docker build -t tornado-websocket .
docker run -it tornado-websocket 
``` 
