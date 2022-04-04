from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware


from auth.jwt_bearer import JWTBearer
from routes.goal import router as GoalRouter
from routes.admin import router as AdminRouter
from routes.progress import router as ProgressRouter

app = FastAPI()

origins = [
    "*",
]

token_listener = JWTBearer()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}


app.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
app.include_router(GoalRouter, tags=["Goals"], prefix="/goal") #dependencies=[Depends(token_listener)])
app.include_router(ProgressRouter, tags=["Progresses"], prefix="/progress")