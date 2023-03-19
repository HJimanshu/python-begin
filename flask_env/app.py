from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def hello_world():
    # msg="Hello world"
    return render_template('index1.html')
# @app.route('/Welcome')
# def User():
#     msg1="Welcome to my world"
#     return
if __name__ == '__main__':
    app.run(debug =True,port=8000)