#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        t = request.form.get("txt")
        responce = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": t}])
        r = responce["choices"][0]["message"]["content"]
        return(render_template("index.html",result=r))
    else:
        return(render_template("index.html",result="waiting"))

if __name__ == "__main__":
    app.run()


# In[ ]:




