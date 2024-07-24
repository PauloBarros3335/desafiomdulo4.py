



from flask import Flask # type: ignore

app = Flask(__name__)

@app.route('/ ')
def index():
    return 'Meu projeto em Python Do desavio da CesarSchool em noções de Programação, está fucionando perfeitamente!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    