from flask import Flask,render_template,request

from openai import OpenAI

# Set OpenAI API key and model
import os
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        q = request.form.get("txt")
        r = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "user", "content": q}],
        )
        return(render_template("index.html",result=r.choices[0].message.content))
    else:
        return(render_template("index.html",result="waiting"))

if __name__ == "__main__":
    app.run()




