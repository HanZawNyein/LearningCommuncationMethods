import grpc
import logging
import time
from concurrent import futures
from todo_service import TodoServicer, todo_pb2_grpc

logging.basicConfig(level=logging.INFO)
# Create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# Add the TodoServicer to the server
todo_pb2_grpc.add_TodoServiceServicer_to_server(TodoServicer(), server)

# Start the server
server.add_insecure_port('[::]:50051')
server.start()
logging.info("Server started on port 50051")
server.wait_for_termination()
