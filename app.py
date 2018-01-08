from flask import Flask, render_template, json, request , jsonify
app = Flask(__name__)

@app.route('/login',methods=['POST'])
def signUp():
    # read the posted values from the UI
    _name = request.form['email']
    _email = request.form['password']
    print(_name)
    print(_email)
    return "Hello"


@app.route('/welcome')
def welcome():
    return 'welcome'


@app.route('/user')
def get_current_user():
    return jsonify(
        username='Wassim',
        email='wassim04@gmail.com',
    )
if __name__ == "__main__":
    app.run()
