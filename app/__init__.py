from .main import app
from .routers import exercises
app.include_router(exercises.router)
