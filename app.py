from datetime import datetime
import os
from flask import Flask, request  
app = Flask(__name__)




@app.route("/")
def fill_form():  
    return '''  
        <h1>Call the API and Get the data</h1>  
        <form method="post" action="/getdata">  
             
            <input type="submit" value = "Click Here To Fetch API Data" >  
        </form>   
        ''' 

@app.route("/getdata", methods=["POST"])  
def api_call():  
    response = requests.get(f"https://catfact.ninja/fact").json()
    print(response)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y%H:%M:%S")
    container_client.upload_blob(dt_string, response['fact'])
    return "<p>Uploaded: {}</p>".format(response) 
