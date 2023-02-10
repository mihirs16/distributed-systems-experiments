import flask
import grpc_client
from MatrixMult_pb2 import MatrixRequest

app = flask.Flask(__name__)


@app.get("/")
def homepage():
    return '<a href="/add">add</a> or <a href="/multiply">multiply</a>'


@app.get("/add")
def add():
    A = [[1, 2], [5, 6]]
    B = [[1, 2], [5, 6]]
    return grpc_client.addMatrix(A, B)


@app.get("/multiply")
def multiply():
    A = [[1, 2], [5, 6]]
    B = [[1, 2], [5, 6]]
    return grpc_client.multMatrix(A, B)

