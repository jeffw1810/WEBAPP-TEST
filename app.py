import os
from azure.storage.blob import BlobServiceClient
from datetime import datetime
from flask import Flask, request  
import requests
app = Flask(__name__)


connect_str = 'DefaultEndpointsProtocol=https;AccountName=saadstorage223344;AccountKey=M/AKSOBtwvfzwiku44/J4cHEBJgGZU+v8SHJU7Q2xns0WgiNwhnqKuowWCBx8IJDk2VHDs2n7kDL+AStMYJ4ig==;EndpointSuffix=core.windows.net'
container_name = "mycontainer"
blob_service_client = BlobServiceClient.from_connection_string(conn_str=connect_str) # create a blob service client to interact with the storage account
try:
    container_client = blob_service_client.get_container_client(container=container_name) # get container client to interact with the container in which images will be stored
    container_client.get_container_properties() # get properties of the container to force exception to be thrown if container does not exist
except Exception as e:
    container_client = blob_service_client.create_container(container_name) # create a container in the storage account if it does not exist


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

if __name__ == '__main__':
   app.run(debug=True)
