from flask import Flask, escape, request, render_template
from pyPdf import PdfFileWriter, PdfFileReader
import requests
app = Flask(__name__)

@app.route('/')
def myform():
    return render_template('html_file.html')

@app.route('/', methods=['POST'])


def apod():
        render_template('html_file.html')
        akey=open(api_key)
        key=akey.read()
        year = request.form['year']
        month = request.form['month']
        day = request.form['day']
        url=f'https://api.nasa.gov/planetary/apod?date={year}-{month}-{day}&api_key={key}'
        response=requests.get(url, allow_redirects=True)
        open("filename.jpg","wb").write(response.content)
        output_img = PdfFileWriter()
        if (response.status_code) == 404:
                print(response.status_code)
        download = input('Download as pdf')
        if download == True:
                file = PdfFileReader(open(filename,"rb"))#filename is the file in which the image is.
                for i in range(0,file.getNumPages()):
                            output_img.addPage(file.getPage(i))
if __name__ == '__main__':
    app.run()
        
