import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from monarch_api import association, entity, histopheno, search

PREFIX = "/v3/api"
app = FastAPI(docs_url="/v3/docs", redoc_url=None)
# app = FastAPI(docs_url=None, redoc_url='/v3/docs')
app.include_router(entity.router, prefix=f"{PREFIX}/entity")
app.include_router(association.router, prefix=f"{PREFIX}/association")
app.include_router(search.router, prefix=PREFIX)
app.include_router(histopheno.router, prefix=f"{PREFIX}/histopheno")

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def _root():
    return RedirectResponse(url="/v3/docs")


@app.get("/api")
async def _api():
    return RedirectResponse(url="/v3/docs")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)