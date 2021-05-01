from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id':1,
        'title':U'Buy Groceries',
        'description':U'Make chesse, pizza, fruits',
        'done':False,
    },
    {
        'id':2,
        'title':U'Learn Python',
        'description':U'Need to find a good python tutorial',
        'done':False, 
    },
]

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/get-data")
def get_tasks():
    return jsonify({
        "data":tasks,
    })
@app.route("/add-data", methods = ["POST"])
def add_tasks():
    if not request.json:
        return jsonify({
            "status":"Error",
            "message":"Please Provide the Data"
        }, 400)
    task = {
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',[]),
        'done':False, 
    }
    tasks.append(task) 
    return jsonify({            
        "status":"Success",
        "message":"Task added Successfully"
        })

if(__name__=="__main__"):
    app.run(debug = True)

