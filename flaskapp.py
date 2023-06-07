from flask import Flask,jsonify,request

app=Flask(__name__)
List = [
    {
        "Contact":u"8975852889",
        "Name":u"Adi",
        "done":False,
        "id":1,
    },
    {
         "Contact":u"1345678954",
        "Name":u"Amy",
        "done":False,
        "id":2,
    }
]
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"pls provide the data"
        },400)
    contact={
        "id":List[-1]["id"]+1,
        "Name":request.json["Name"],
        "Contact":request.json.get("Contact",""),
        "done":False
    }
    List.append(contact)
    return jsonify({
        "status":"success",
        "message":"contact added successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":List
    })

if (__name__=="__main__"):
    app.run(debug=True)