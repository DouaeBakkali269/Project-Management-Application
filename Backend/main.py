
from fastapi import FastAPI
from routers import users, projects, tasks, auth
from database import Base, engine


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(projects.router)
app.include_router(tasks.router)
app.include_router(auth.router)



