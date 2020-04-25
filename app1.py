 
from flask import *

app = Flask(__name__)

@app.route('/')
def manipage():
    return render_template('templets\1234.html')

if __name__ == '__main__': 
    ##app.run(debug=True)
    (app.debug==True)
    app.run()
    