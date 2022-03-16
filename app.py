from fastapi import FastAPI, Depends

from auth.jwt_bearer import JWTBearer
from routes.goal import router as GoalRouter
from routes.admin import router as AdminRouter

app = FastAPI()

token_listener = JWTBearer()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}


app.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
app.include_router(GoalRouter, tags=["Goals"], prefix="/goal") #dependencies=[Depends(token_listener)])
