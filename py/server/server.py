import time
import grpc
from proto import hello_pb2_grpc, hello_pb2
from concurrent import futures

ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Server(hello_pb2_grpc.SayHelloServicer):
    def __init__(self):
         pass
    
    def SayHello(self, request, context):
        result = "Hello,"+ request.requestname
        return hello_pb2.HelloResponse(responseMsg = str(result))
    
def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_SayHelloServicer_to_server(Server(), server)
    server.add_insecure_port('[::]:50002')
    server.start()
    print("start service...listen port:50002")
    try:
        while True:
                time.sleep(ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
    
if __name__ == "__main__":
    run()