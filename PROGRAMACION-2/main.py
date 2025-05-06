from flask import Flask, render_template, request
import requests

app= Flask(__name__)

def clima_dato(city:str):
    API_KEY= "a5351cfb5b1784a25423913acc11771b"
    idioma= "es"
    url= f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang={idioma}&appid={API_KEY}"
    r = requests.get(url).json()
    print(r)
    return r

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('clima.html')
    if request.method == 'POST':
        ciudad= request.form.get('txt_ciudad')
        if ciudad !='' :
            r = clima_dato(ciudad)
            print('HOLA SOY UN POST ' ,  r)
            coor = r.get('coord')
            weather = r.get('weather')[0]
            main = r.get('main')
            return render_template('clima.html', weather = weather, c = ciudad, coor = coor, main= main, by = 'Fernando Cabrera')
        return render_template('clima.html')



if __name__ == "__main__":
    app.run(debug=True)