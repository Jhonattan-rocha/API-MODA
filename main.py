import json
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import database
from app.routers import (categoryRouter)
from app.routers.DefaultRouters import companyRouter, subCategoryRouter, productCategoryRouter, personRouter, \
    productRouter, userRouter, userProfileRouter, permissionsRouter, tokenRouter, employeeRouter, inputOutputStockRouter, fileRouter
from app.routers.CustomRouters import (dynamicFieldValueRouter, dynamicEntityRouter, dynamicFieldRouter,
                                       genericRouter)
import os
from uvicorn.config import LOGGING_CONFIG
import globals

# Função para gerar uma chave AES e IV
def generate_aes_key_and_iv():
    aes_key = os.urandom(32)  # Chave AES de 256 bits
    iv = os.urandom(12)  # IV de 96 bits para AES-GCM
    return aes_key, iv

# Cria as tabelas no banco de dados
@asynccontextmanager
async def lifespan_startup(app: FastAPI):
    aes_key, iv = generate_aes_key_and_iv()
    globals.aes_key = aes_key
    globals.iv = iv
    app.include_router(categoryRouter)
    app.include_router(productRouter)
    app.include_router(productCategoryRouter)
    app.include_router(subCategoryRouter)
    app.include_router(personRouter)
    app.include_router(companyRouter)
    app.include_router(dynamicEntityRouter)
    app.include_router(dynamicFieldRouter)
    app.include_router(dynamicFieldValueRouter)
    app.include_router(genericRouter)
    app.include_router(userRouter)
    app.include_router(userProfileRouter)
    app.include_router(permissionsRouter)
    app.include_router(employeeRouter)
    app.include_router(tokenRouter)
    app.include_router(inputOutputStockRouter)
    app.include_router(fileRouter)
    generate_doc()
    async with database.engine.begin() as conn:
        await conn.run_sync(database.Base.metadata.create_all)

    yield


def generate_doc():
    with open("openapi.json", "w") as f:
        json.dump(app.openapi(), f, indent=4)


app = FastAPI(lifespan=lifespan_startup,
              title="ModaBrasileira",
              description="API under development",
              summary="Routes of app",
              version="0.0.1",
              terms_of_service="http://example.com/terms/",
              contact={
                  "name": "Jhonattan Rocha da Silva",
                  "url": "http://www.example.com/contact/",
                  "email": "jhonattab246rocha@gmail.com",
              },
              license_info={
                  "name": "Apache 2.0",
                  "identifier": "MIT",
              })

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5173",
    "http://10.0.0.101:8080",
    "*"
]

app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=origins,  # Permite essas origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Configuração do formato do log
LOGGING_CONFIG["formatters"]["access"] = {
    "()": "uvicorn.logging.AccessFormatter",
    "fmt": "%(asctime)s - %(levelname)s - %(client_addr)s - %(request_line)s - %(status_code)s",
}

# Configuração do handler para salvar os logs em arquivo
LOGGING_CONFIG["handlers"]["file"] = {
    "class": "logging.FileHandler",
    "filename": "access.log",  # Nome do arquivo de log
    "formatter": "access",
}

# Adiciona o novo handler no logger de acesso
LOGGING_CONFIG["loggers"]["uvicorn.access"] = {
    "level": "INFO",
    "handlers": ["file"],  # Define que o log de acesso será salvo no arquivo
    "propagate": False,
}

if __name__ == "__main__":
    import uvicorn
    import sys

    uvicorn.run("main:app", host=sys.argv[1], port=8081, reload=True, log_config=LOGGING_CONFIG, proxy_headers=True)
