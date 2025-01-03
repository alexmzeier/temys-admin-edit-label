from appwrite.client import Client
from appwrite.services.users import Users
from appwrite.exception import AppwriteException
import os
import json
from urllib.parse import parse_qs

# This Appwrite function will be executed every time your function is triggered
def main(context):
    # You can use the Appwrite SDK to interact with other services
    # For this example, we're using the Users service

    userId = context.req.headers["x-appwrite-user-id"]
    
    data = json.loads(context.req.body)
    label = data['label']
    
    client = (
        Client()
        .set_endpoint(os.environ["APPWRITE_FUNCTION_API_ENDPOINT"])
        .set_project(os.environ["APPWRITE_FUNCTION_PROJECT_ID"])
        .set_key(os.environ["APPWRITE_FUNCTION_API_KEY"])
    )
    users_service = Users(client)

    try:
        # Erstelle einen neuen Benutzer
        users_service.update_labels(
            userId,
            [ label ]
        )
                
        response = {
            "status": "ok",
            "message": "label updated"
        }
    except Exception as e:
        response = {
            "status": "error",
            "message": str(e)
        }
        
    response = {
            "status": "ok",
            "message": "label updated"
        }
    
    return context.res.json(response)
