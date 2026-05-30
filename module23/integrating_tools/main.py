from fastapi import FastAPI
from model import Developer, Projects

app = FastAPI()

@app.post("/developer/")
def create_developer(developer: Developer):
    return {"message": "Developer created successfully", "developer": developer}


@app.post("/projects/")
def create_project(project: Projects):
    return {"message": "Project created successfully", "project": project}



@app.get("/projects/")
def get_projects():
    sample_project = Projects(
         title = "Sample Project",
         description = "This is a sample project",
         language = ["HTML","CSS","JAVASCRIPT"],
         lead_developer = Developer(name="John Doe",experience=5)
    )