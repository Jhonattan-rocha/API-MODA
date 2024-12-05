import json
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        
        # Captura os dados da requisição
        request_body = await request.body()
        action = "Criar" if request.method.lower() == "post" else "Editar" if request.method.lower() == "put" or request.method.lower() == "patch" else "Deletar"
        request_data = {
            "method": request.method,
            "url": str(request.url),
            "headers": dict(request.headers),
            "body": request_body.decode('utf-8') if request_body else None,
            "action": action,
            "type": "request"
        }
        
        with open("requests.log", "a+") as file:
            json.dump(file, request_data)
        
        # Processa a requisição
        response = await call_next(request)

        # Captura os dados da resposta
        response_data = {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "action": action,
            "type": "response"
        }

        with open("requests.log", "a+") as file:
            json.dump(file, response_data)
        
        return response
