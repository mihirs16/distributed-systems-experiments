from concurrent import futures

import grpc
import MatrixMult_pb2, MatrixMult_pb2_grpc

class MatrixServicer (MatrixMult_pb2_grpc.MatrixServiceServicer):

    def AddBlock(self, request, context):
        print("Add Block Request: \n", request)
        C00 = request.a00 + request.b00
        C01 = request.a01 + request.b01
        C10 = request.a10 + request.b10
        C11 = request.a11 + request.b11

        return MatrixMult_pb2.MatrixReply(
            c00 = C00, c01 = C01,
            c10 = C10, c11 = C11
        )

    def MultiplyBlock(self, request, context):
        print("Multiply Block Request: \n", request)
        C00 = (request.a00 * request.b00) + (request.a01 * request.b10)
        C01 = (request.a00 * request.b01) + (request.a01 * request.b11)
        C10 = (request.a10 * request.b00) + (request.a11 * request.b10)
        C11 = (request.a10 * request.b01) + (request.a11 * request.b11)
        
        return MatrixMult_pb2.MatrixReply(
            c00 = C00, c01 = C01,
            c10 = C10, c11 = C11
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    MatrixMult_pb2_grpc.add_MatrixServiceServicer_to_server(MatrixServicer(), server)
    server.add_insecure_port('[::]:50051')

    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()