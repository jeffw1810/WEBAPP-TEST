from flask import Flask
app = Flask(__name__)

@app.route("/")
def fill_form():  
    return '''  
        <h1>Call the API and Get the data</h1>  
        <form method="post" action="/getdata">  
             
            <input type="submit" value = "Click Here To Fetch API Data" >  
        </form>   
        ''' 
