# Simple async socket app without using third-party libraries with not blocking IO operations. 

## Commands

To run server
```shell
python -m src.presentation.server.main
```
To run client
```shell
python -m src.presentation.client.main
```
To delete all messages in src.presentation.messages
```shell
python -m src.infrastructure.clean_messages.main
```
Or you can use `make` command

`up-server` To run server \
`up-client` To run client \
`clear-messages` To delete all messages


All messages from user to server and from server to user stored in `src.presentation.messages`.
It was done so that notifications from the user or server wouldn't block the input stream, 
which operates in parallel with the rest of the program.

