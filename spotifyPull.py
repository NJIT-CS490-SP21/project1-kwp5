import requests
import os, random
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def getTrackInfo():
    load_dotenv(find_dotenv())

    AUTH_URL = 'https://accounts.spotify.com/api/token'
    
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET'),
    })
    
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    
    artist_ids = ['1t20wYnTiAT0Bs7H1hv9Wt','5JZ7CnR6gTvEMKX4g70Amv','5IH6FPUwQTxPSXurCrcIov']
    id_num = artist_ids[random.randint(0,2)]
    
    BASE_URL = 'https://api.spotify.com/v1/artists/'+ id_num +'/top-tracks'
    
    headers = {
        'Authorization': 'Bearer ' + access_token,
    }
    
    response = requests.get(BASE_URL, headers=headers)
    data = response.json()
    refined_data = [data['tracks']['name'], data['tracks']['artists']['name'], data['tracks']['images'], data['tracks']['previw_url']]
    return render_template(
        "index.html",
        track_data=refined_data
    )
    
app.run(
    port=int(os.getenv('PORT',8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)