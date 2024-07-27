from flask import Flask, render_template,request,session,redirect,url_for
from forms import InputForm

# インスタンス生成
app = Flask(__name__)
app.secret_key = b"hit"

@app.route("/",methods=["GET","POST"])
def input():
    form = InputForm()

    # POST
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['email'] = form.email.data
        return redirect(url_for('output'))

    # GET
    if 'name' in session:
        form.name.data = session['name']
    if 'email' in session:
        form.email.data = session['email']
    
    return render_template("pages/input.html",form=form)

@app.route("/output",methods=["GET","POST"])
def output():
    return render_template("pages/output.html")

if __name__ == "__main__":
    # デバッグモード
    app.debug = True
    # ホストとポートの指定
    # WEBサーバー実行
    app.run(host="0.0.0.0",port=5002)