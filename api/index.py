from flask import Flask ,jsonify
import socket
import random;
import json
import requests 
# Inside api/quotes.py
def handler(request):
    return {
        "statusCode": 200,
        "body": "Stay positive and keep going!"
    }
app=Flask(__name__)
# Loading json
with open('quotes.json','r')as f:
    jquotes=json.load(f)

#get all quotes
@app.route('/api/quotes',methods=['GET'])


def all_quote():
    return  jsonify(jquotes)


#random quotes
@app.route('/api/quotes/random',methods=['GET'])
def get_random_quote():
     return  jsonify(random.choice(jquotes))

#random quotes by number
@app.route('/api/quotes/random/<int:index>',methods=['GET'])
def get_random_quote_number(index):

        return jsonify(random.sample(jquotes,index))

#get quotes by index
@app.route('/api/quotes/<int:index>',methods=['GET'])
def get_quote_by_index(index):
        if 0<index<len(jquotes):
             return jsonify(jquotes[index])
        return jsonify([{"error":"Quotes Not Found :("}])

 #owner 
@app.route('/api/owner',methods=['GET'])
def owner():
  return jsonify([{"Author":"Developed By Subham Sinha"},
                  {
       "GitHub":"subhamsinhadev"
  }])
        

        

    
if __name__== '__main__':
    host=socket.gethostbyname(socket.gethostname())
    app.run(debug=True,host="0.0.0.0",port=5000)
