# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small, working REST API using FastAPI to manage a collection of tasks or books. This assignment helps students learn how to define routes, validate request data with Pydantic, return JSON responses, and test API endpoints.

## 📝 Tasks

### 🛠️ Set Up a FastAPI App

#### Description
Create a new FastAPI application and add a root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Create an app instance using `FastAPI()`.
- Define a `GET /` route that returns a JSON welcome message.
- Run the app locally with `uvicorn`.
- Confirm the app responds successfully in the browser or with a tool like `curl`.
- Example response:
  ```json
  {"message": "Welcome to the Task API!"}
  ```

### 🛠️ Build CRUD Endpoints for a Resource

#### Description
Create an API for managing tasks with endpoints for listing, creating, retrieving, updating, and deleting items.

#### Requirements
Completed program should:

- Define a `Task` model with fields such as `id`, `title`, and `description`.
- Store tasks in memory while the server is running.
- Implement `GET /tasks` to return all tasks.
- Implement `POST /tasks` to create a new task.
- Implement `GET /tasks/{task_id}` to fetch a single task.
- Implement `PUT /tasks/{task_id}` to update an existing task.
- Implement `DELETE /tasks/{task_id}` to remove a task.
- Return appropriate HTTP status codes such as `200`, `201`, and `404`.
- Validate input so a task title cannot be empty.
- Example request body:
  ```json
  {
    "title": "Finish project proposal",
    "description": "Draft the final project summary for class."
  }
  ```

### 🛠️ Test Your API

#### Description
Use FastAPI’s interactive docs or a client to verify the behavior of each endpoint.

#### Requirements
Completed program should:

- Open the automatically generated Swagger UI at `/docs`.
- Test creating a task and retrieving the list of tasks.
- Confirm the API returns JSON in the expected format.
- Document one example request and response in comments or a brief note.
