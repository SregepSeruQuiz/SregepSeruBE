from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers.user import router_login
from api.routers.quizCustom import router_quizcustom
from api.routers.quizUmum import router_quizumum

app = FastAPI(docs_url="/docs", title="SregepSeru")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "http://localhost:8000/docs"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_login)
app.include_router(router_quizcustom)
app.include_router(router_quizumum)
