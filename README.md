# oknext-server
Based on python lib [simple-websocket-server](https://github.com/pikhovkin/simple-websocket-server/).

## requirements
lib above

## conf
you need to generate ssl certificates: `openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout key.pem`

make sure they are in the same dir as the script

## behaviour
basically broadcasts everything to all clients
