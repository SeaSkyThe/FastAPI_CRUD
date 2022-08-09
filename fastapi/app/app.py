from fastapi import FastAPI

app = FastAPI()

#GET REQUEST
@app.get('/', tags=['ROOT'])
async def root() -> dict:
    return{"Ping":"Pong"}

# GET --> Read todo
@app.get('/todo', tags=['todos'])
async def get_todo() -> dict:
    return {"data": todos}

# POST --> Create todo
@app.post('/todo', tags=['todos'])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return{
        "data": "A todo has been added!"
    }
# PUT --> Update todo
@app.put('/todo/{id}', tags=['todos'])
async def update_todo(id:int, body:dict) -> dict:
    for todo in todos:
        if(int(todo['id']) == id):
            todo['Activity'] = body['Activity']
            return {
                "data": f"Todo with id {id} has been updated."
            }
    return {
        "data": f"Todo with id {id} was not found."
    }
# DELETE --> Delete todo
@app.delete('/todo/{id}', tags=['todos'])
async def delete_todo(id:int) -> dict:
    for todo in todos:
        if(int(todo['id']) == id):
            todos.remove(todo)
            return{
                "data": f"Todo with id {id} has been deleted"
            }
    return {
        "data": f"This todo with id {id} wasn't found!"
    }




todos = [
    {
        "id": 1,
        "Activity": "Play with friends tonight"
    },
    {
        "id": 2,
        "Activity": "Work out"  
    }
]