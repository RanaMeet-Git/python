from fastapi import FastAPI
app = FastAPI()

@app.get("/students")
def students():
    return ["Ravi","Rahul","Anjali"]

@app.get("/students/{student_id}")
def student(student_id: int):
    return {"student_id": student_id}


@app.get("/students/{class_id}/{student_id}")
def get_student(class_id:int, student_id:int):
    return {
        "class":class_id,
        "student":student_id
    }