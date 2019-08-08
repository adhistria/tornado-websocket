## Description

Simple Program with 3 Api To Send Message

## Dev Environment Setup

### Python3
Install python using homebrew
```
brew install python3
```

Or you can install python from the source, please go to the following link. 
[Install Python 3](https://www.python.org/downloads/release/python-374/)  

### Install packages
Run the following command
```
pip install -r requirements.txt
```

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
python main.py
``` 

## How to run the test
Run the following command
```
nosetests
``` 
