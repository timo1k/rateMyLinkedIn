from flask import Flask, redirect, url_for, request
from linkedInScript import getGPT
app = Flask(__name__)

@app.route('/success/<user>/<passw>')
def success(user, passw):
   answer = getGPT()
   return '%s' % (answer)

@app.route('/error')
def error():
   return 'error'

@app.route('/login', methods=['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['user']
      passw = request.form['pass']
      if (len(user) == 0 or len(passw) == 0 ):
         return redirect(url_for('error'))
      else:
         
         return redirect(url_for('success', user=user, passw=passw))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success', user=user))

if __name__ == '__main__':
   app.run(debug=True, port=8080)
