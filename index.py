# from flask import Flask ,render_template;
from flask import Flask;
from flask import render_template;

app=Flask(__name__);

@app.route("/")
def printthis():
    return render_template("index.html");
    # return "hello this";


# app.run(host="127.0.0.1",debug=True,use_reloader=False)
# if __name__=="main":
#     app.run(host="127.0.0.1",debug=True)