# gRPC with REST

Experiment for gRPC with REST using Flask in python.

## How to run

- Setup environment

```bash
# setup python
python -m venv venv
python -m pip install -r requirements.txt

# setup gRPC and protobuf classes
python -m grpc_tools.protoc -I./proto/ --python_out=. --pyi_out=. --grpc_python_out=. ./proto/MatrixMult.proto
```

- gRPC Server

```bash
python grpc_server.py
```

- Flask Server (gRPC Client)

```bash
python grpc_flask.py
```

## Legacy

- To run experiment from [gRPC with Java](/gRPC/) for Python

```bash
python grpc_client.py
```
