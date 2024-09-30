from flask import Flask

app = Flask(__name__)

lastrequest = ""

@app.route('/getlastrequest')
def index():
    return lastrequest

@app.route('/dorequest/<request>')
def dorq(request):
    global lastrequest
    lastrequest=request
    return "{success: \"true\"}"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
