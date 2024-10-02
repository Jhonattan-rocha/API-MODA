import json
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import database
from app.routers import (categoryRouter)
from app.routers.DefaultRouters import companyRouter, subCategoryRouter, productCategoryRouter, personRouter, \
    productRouter, userRouter, userProfileRouter, permissionsRouter, tokenRouter, employeeRouter
from app.routers.CustomRouters import (dynamicFieldValueRouter, dynamicEntityRouter, dynamicFieldRouter,
                                       genericRouter)


# Cria as tabelas no banco de dados
@asynccontextmanager
async def lifespan_startup(app: FastAPI):
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

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="10.150.0.56", port=8081, reload=True)
