from flask import Flask, render_template, request #Importar a classe Flask
import backend

app = Flask(__name__) # Cria objeto app

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        text = request.form.get('textbox')
        #text = 4
        return render_template("index.html", 
        output = backend.metro_pes(float(text)),
        user_text = text)

if __name__ == "__main__":
    app.run()
    
print(text)