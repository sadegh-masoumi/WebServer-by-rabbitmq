from fastapi import APIRouter
from .models import Data
from rpc.rpc_client import FibonacciRpcClient

fibonacci_rpc = FibonacciRpcClient()

router = APIRouter()


@router.get("/")
def test():
    return "API is running"


@router.post("/calculate")
def calculate_fibonacci(inputData: Data):
    print(" [x] Requesting fib(%s)" % inputData.fibNumber)
    response = fibonacci_rpc.call(inputData.fibNumber)
    print(" [.] Got %r" % response)

    return response
