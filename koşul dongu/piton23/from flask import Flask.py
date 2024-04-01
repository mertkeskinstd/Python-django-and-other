from flask import Flask

# Flask uygulamasını oluşturun
app = Flask(__name__)

# Kök dizin için bir rota ve işlev tanımlayın
@app.route('/')
def hello_world():
    return 'Merhaba Dünya!'

# Web uygulamasını çalıştırın
if __name__ == '__main__':
    app.run()
