# Spotify Artist and Track Search with Genius Support
#### Made By: Kyle Partyka
#### Github: https://github.com/kwp5
#### App Demo: https://cs490-project1-kwp5.herokuapp.com/
### <ins>Technologies Used</ins>: Python, HTML5, CSS, Spotify API, Genius API, Heroku (For app deployment) <br>
### <ins>Libraries Used</ins>: Flask, Dotenv, Requests, os <br>
### <ins>How To Run</ins>:
  1. Install all technologies or libraries
  2. Create accounts for spotify and genius api to access authentication keys
  3. In local repo create an .env file for api authentication and not be pushed to github/heroku <br>
    3.1 Should include export for Spotify CLIENT_ID, CLIENT_SECRET, and Genius G_ACCESS_TOKEN
  4. Run spotifyPull.py <br>
    4.1. For heroku deployment have heroku installed and create a new app with: <br>
               ```     heroku login -i ``` <br>
               ```     heroku create {insert name or leave blank} ``` <br>
               ```     git push heroku main  ```<br>
    4.2. In heroku you must go into the settings of the app and add the .env variables in the config vars
---
### <ins>Tech Issues<ins>:
  1. CSS was only doing some of the changes that I had put into the file <br>
  ~ At first I spent time just making small changes in another online compiler to test and debug any issues. I wanted to fix it so I began searching google for other issues that would be reated to it. First was if there was any problem with the html linking of the css file and I adjusted some things to test and nothing was changing. I then searched for the same problem in cloud9 or aws to see if that was the issue. I found nothing there and then just scanned through my css file again to see if there was any problem that would make the page fail. Finding nothing I changed the css filename back to what it originally was, style.css, rather than "proj1Style.css" and it now works perfectly fine. <br> 
  2. Implementing genius api <br>
  ~ It took me some time to really understand how genius was supposed to be implemented into the python code due to the lack of information that the genius api provides with authentication. I tried to copy the spotify authentication and match it the best I could to ensure that I would have access to the json data. That solution did not last long and then I went to google to try to find an example of someone implementing the api. On stackoverflow I was able to see people using their full authentication code and others just using the access token. So i matched the code with the information without authentication and it worked. <br>
  3. Adding user input <br>
  ~ Adding user input took time because I needed to look up the flask documentation as well as consult stackoverflow with questions regarding the translation of data to another flask app page. It was more researching than debugging but when it came to the code there were many different optinos that I saw people do and what the documentation provides, but I found the way that I stuck with through the bottom end of the documentation. <br>
  ~ <ins>Links</ins>: <br>
        https://flask.palletsprojects.com/en/1.1.x/quickstart/#accessing-request-data <br>
        https://www.tutorialspoint.com/flask/flask_quick_guide.htm <br>
 ---
### <ins>Future Additions<ins>:
  1. Add a permanent search bar at the top of the page for continuous searching instead of having to press the back button to continue to search <br>
    ~ Could be done by the entire page operating through the same route and when the submit button is pressed it would rerun the route with the new information
  2. Use javascript and more css to mimic Spotify's current UI where the songs would be on a slideshow showing the top song first. User would click the arrow to see the next song and make the UI more engaging for the user rather than a list
