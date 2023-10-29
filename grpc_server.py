import grpc
import logging
from concurrent import futures

from todo_service import todo_pb2_grpc

logging.basicConfig(level=logging.INFO)
class TodoServicer(todo_pb2_grpc.TodoServiceServicer):
    ...


# Create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# Add the TodoServicer to the server
todo_pb2_grpc.add_TodoServiceServicer_to_server(TodoServicer(), server)

# Start the server
server.add_insecure_port('[::]:50051')
server.start()
logging.info("Server started on port 50051")

# Wait for the server to stop
try:
    while True:
        ...
except KeyboardInterrupt:
    server.stop(0)
