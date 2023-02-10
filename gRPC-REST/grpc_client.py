import grpc
import MatrixMult_pb2_grpc
from MatrixMult_pb2 import MatrixRequest, MatrixReply


def MutliplyMatrix (stub: MatrixMult_pb2_grpc.MatrixServiceStub):
    A = [
        [1, 2, 3, 4], 
        [5, 6, 7, 8], 
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    B = [
        [1, 2, 3, 4], 
        [5, 6, 7, 8], 
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    A3M1 = stub.MultiplyBlock(MatrixRequest(
        a00 = A[0][0], a01 = A[0][1],
        a10 = A[1][0], a11 = A[1][1],
        b00 = B[0][0], b01 = B[0][1],
        b10 = B[1][0], b11 = B[1][1]
    ))

    A3M2 = stub.MultiplyBlock(MatrixRequest(
        a00 = A[0][2], a01 = A[0][3],
        a10 = A[1][2], a11 = A[1][3],
        b00 = B[2][0], b01 = B[2][1],
        b10 = B[3][0], b11 = B[3][1]
    ))

    A3 = stub.AddBlock(MatrixRequest(
        a01 = A3M1.c01,
        a00 = A3M1.c00,
        a10 = A3M1.c10,
        a11 = A3M1.c11,
        b00 = A3M2.c00,
        b01 = A3M2.c01,
        b10 = A3M2.c10,
        b11 = A3M2.c11
    ))

    B3M1 = stub.MultiplyBlock(MatrixRequest(
        a00 = A[0][0], a01 = A[0][1],
        a10 = A[1][0], a11 = A[1][1],
        b00 = B[0][2], b01 = B[0][3],
        b10 = B[1][2], b11 = B[1][3]
    ))

    B3M2 = stub.MultiplyBlock(MatrixRequest(
        a00 = A[0][2], a01 = A[0][3],
        a10 = A[1][2], a11 = A[1][3],
        b00 = B[2][2], b01 = B[2][3],
        b10 = B[3][2], b11 = B[3][3]
    ))

    B3 = stub.AddBlock(MatrixRequest(
        a00 = B3M1.c00,
        a01 = B3M1.c01,
        a10 = B3M1.c10,
        a11 = B3M1.c11,
        b00 = B3M2.c00,
        b01 = B3M2.c01,
        b10 = B3M2.c10,
        b11 = B3M2.c11
    ))

    C3M1 = stub.MultiplyBlock(MatrixRequest(
        a00 = A[2][0], a01 = A[2][1],
        a10 = A[3][0], a11 = A[3][1],
        b00 = B[0][0], b01 = B[0][1],
        b10 = B[1][0], b11 = B[1][1]
    ))

    C3M2 = stub.MultiplyBlock(MatrixRequest(
        a00 = A[2][2], a01 = A[2][3],
        a10 = A[3][2], a11 = A[3][3],
        b00 = B[2][0], b01 = B[2][1],
        b10 = B[3][0], b11 = B[3][1]
    ))

    C3 = stub.AddBlock(MatrixRequest(
        a00 = C3M1.c00,
        a01 = C3M1.c01,
        a10 = C3M1.c10,
        a11 = C3M1.c11,
        b00 = C3M2.c00,
        b01 = C3M2.c01,
        b10 = C3M2.c10,
        b11 = C3M2.c11
    ))

    D3M1 = stub.MultiplyBlock(MatrixRequest(
        a00 = A[2][0], a01 = A[2][1],
        a10 = A[3][0], a11 = A[3][1],
        b00 = B[0][2], b01 = B[0][3],
        b10 = B[1][2], b11 = B[1][3]
    ))

    D3M2 = stub.MultiplyBlock(MatrixRequest(
        a00 = A[2][2], a01 = A[2][3],
        a10 = A[3][2], a11 = A[3][3],
        b00 = B[2][2], b01 = B[2][3],
        b10 = B[3][2], b11 = B[3][3]
    ))

    D3 = stub.AddBlock(MatrixRequest(
        a00 = D3M1.c00,
        a01 = D3M1.c01,
        a10 = D3M1.c10,
        a11 = D3M1.c11,
        b00 = D3M2.c00,
        b01 = D3M2.c01,
        b10 = D3M2.c10,
        b11 = D3M2.c11
    ))

    return [
        [A3.c00, A3.c01, B3.c00, B3.c01],
        [A3.c10, A3.c11, B3.c10, B3.c11],
        [C3.c00, C3.c01, D3.c00, D3.c01],
        [C3.c10, C3.c11, D3.c10, D3.c11],
    ]

def run ():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = MatrixMult_pb2_grpc.MatrixServiceStub(channel)
        print(MutliplyMatrix(stub))


if __name__ == "__main__":
    run()