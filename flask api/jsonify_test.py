from flask import Flask, jsonify
#import json

app = Flask(__name__)

@app.route('/user')
def get_users():
    users=[
        {'name':'Ludwik', 'age':28},
        {'name':'Diana', 'age':32},
        {'name':'Dalia', 'age':3},
        {'name':'Leon', 'age':1}
        ]
    #json_dump = json.dumps(users)
    #return(json_dump)    
    return jsonify(users)

if __name__ == "__main__":
    app.run(port=6977)

#jsonify vs json
#shows different font as well as different order in the dictionary