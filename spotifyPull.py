import requests
import os, random
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template("homepage.html")

@app.route('/', methods=["POST"])
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
    
    BASE_URL = 'https://api.spotify.com/v1/search?q=' + request.form['artist_search'] + '&type=artist&limit=1'
    
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    
    response = requests.get(BASE_URL, headers=headers)
    data = response.json()
    try:
        id_num = data['artists']['items'][0]['id']
    except:
        print("Artist does not exist on Spotify")
        return redirect(url_for('main_page'))
    
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