from flask import Flask, escape, request
import requests
app = Flask(__name__)

@app.route('/')


def apod(year,month,day):
        key=api_key.read()
        url=f'https://api.nasa.gov/planetary/apod?date={year}-{month}-{day}&api_key={key}'
        response=requests.get(url, allow_redirects=True)
        if (response.status_code) == 404:
                print(response.status_code)
        download = input('Download as pdf')
        if download == True:
                open('filename.pdf','wb').write(response.content)#filename is the file in which the image is.
if __name__ == '__main__':
    app.run()
        
        
