import requests
import os, random
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def getTrackInfo():
    load_dotenv(find_dotenv())

    SPOT_AUTH_URL = 'https://accounts.spotify.com/api/token'
    
    auth_response = requests.post(SPOT_AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET'),
    })
    
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    
    artist_ids = ['1t20wYnTiAT0Bs7H1hv9Wt','5JZ7CnR6gTvEMKX4g70Amv','5IH6FPUwQTxPSXurCrcIov']
    id_num = artist_ids[random.randint(0,2)]
    
    BASE_URL = 'https://api.spotify.com/v1/artists/'+ id_num +'/top-tracks?market=US'
    
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    
    response = requests.get(BASE_URL, headers=headers)
    data = response.json()
    full_data = []
    track_names = []
    artist_names = []
    track_images = []
    preview_urls = []
    for i in data['tracks']:
        temp_list = []
        for j in i['artists']:
            temp_list.append(j['name'])
        artist_names.append(temp_list)
        track_names.append(i['name'])
        track_images.append(i['album']['images'][0]['url'])
        preview_urls.append(i['preview_url'])
    full_data = [track_names,artist_names,track_images,preview_urls]
    length = len(full_data[3])
    
    BASE_URL = 'https://api.genius.com/search?q='
    
    headers = {
        'Authorization': 'Bearer ' + os.getenv('G_ACCESS_TOKEN')
    }
    lyric_urls = []
    for i in track_names:
        params = {'q': i + " " + artist_names[0][0]}
        response = requests.get(BASE_URL, params=params, headers=headers)
        data = response.json()
        lyric_urls.append(data['response']['hits'][0]['result']['url'])
        
    return render_template(
        "index.html",
        track_data=full_data,
        url_len=length,
        lyrics=lyric_urls,
    )
    
app.run(
    port=int(os.getenv('PORT',8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)