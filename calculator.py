from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates')
app.secret_key = 'secret'

@app.route('/')
def HomePage():
    return "<h1> START CALCULATING </h1>"

@app.route('/+', methods = ['POST', 'GET'])
def addition():
    add = ''
    if request.method=='POST' and 'second' in request.form and 'first' in request.form:
        SN = float(request.form.get('second'))
        FN = float(request.form.get('first'))
        add = (SN + FN)
    return render_template('add.html', add=add)    

if __name__ == '__main__':
    app.run(debug=True)
