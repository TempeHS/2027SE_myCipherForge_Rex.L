from flask import Flask, render_template, request
from engine import encrypt, decrypt

app = Flask(__name__)

@app.route("/")
def index():
      return render_template("index.html")

@app.route("/workshop", methods=["GET", "POST"])
def workshop():
      result = ""
      original = ""
      
      if request.method == "POST":
            try:
                  original = request.form.get("message", "")
                  action = request.form.get("action", "encrypt")
                  
                  if not original.strip():
                        error = "Please enter a message to encrypt"
                  else:
                        key = {
                              "shift": int(request.form.get("shift", 5)),
                              "block_size": int(request.form.get("block_size", 4)),
                              "password": request.form.get("password", "SECRET"),
                              "noise_interval": int(request.form.get("noise_interval", 3)),
                              "noise_char": request.form.get("noise_char", "~")
                        }
                        
                        if action == "encrypt":
                              result = encrypt(original, key)
                        else:
                              result = decrypt(original, key)
            except Exception as e:
                  error = f"Error: {str(e)}"
      return render_template("workshop.html", result=result, original=original, error=error)

if __name__ == "__main__":
      app.run(debug=True, host="0.0.0.0", port=5000)