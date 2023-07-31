from flask import Flask,jsonify,request

app = Flask(__name__)

data = [
    {
        "Contact":"9989874562",
        "Name":"Raju",
        "done":False,
        "id":1
    },
    {
        "Contact":"8789845621",
        "Name":"Rahul",
        "done":False,
        "id":2

    }
]

@app.route("/add-data",methods = ["POST"])

def add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'please provide data',
        },400)
    task = {
        'id':data[-1]['id']+1,
        'Contact':request.json['Contact'],
        'Name':request.json.get('Name',''),
        'done':False
    }
    data.append(task)
    return jsonify({
        'status':'Success',
        'message':'task added successfully'
    })
    
@app.route("/get-data")
def get_task():
    return jsonify({
        'data':data,
    })
    
if(__name__=="__main__"):
    app.run(debug=True)

    