from flask import request

def logger_middleware():
    print(f"[LOG] {request.method} {request.path} - IP:{request.remote_addr}")