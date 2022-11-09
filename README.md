# WebServer By RPC RabbitMq ⚡️
In this project I use RabbitMq & FastApi in a simple example to represent how We can use RabbitMq in our projects. 

# System design diagram
![diagram](https://github.com/sadegh-masoumi/WebServer-by-rabbitmq/blob/main/doc/img/RabbitMQ.png?raw=true)

# Run 🚀
Create RabbitMq Container 👨‍💻
``` bash
docker-compose up -d
```

Run Consumers & WebServers 👨‍💻
``` bash
# run first consumer
python3 rpc/rpc_server.py

# run second consumer
python3 rpc/rpc_server_without_response.py

# run web server
uvicorn app:main --reload
```
HTTP POST Data To "http://localhost:8000/calculator" ⛳️ 🏌️‍♂️ 
``` json
{
    "finNumber": 10
}
```
