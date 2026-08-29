from fastapi import FastAPI

app = FastAPI(title="Task API")

# In-memory list to simulate a database
# tasks = [
#     {"id": 1, "title": "Write API summary", "description": "Describe the main endpoints"}
# ]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API!"}


# TODO: Add a Pydantic model for tasks.
# TODO: Add GET /tasks, POST /tasks, GET /tasks/{task_id}, PUT /tasks/{task_id}, and DELETE /tasks/{task_id}.
# TODO: Validate input so titles are not empty.
