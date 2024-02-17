from flask import Flask,render_template,request

from openai import OpenAI

client = OpenAI(
    api_key="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",
)

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




