#!/home1/arielma1/python/bin/python

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('index.html', name = 'Ozair')

if __name__ == '__main__':
  app.run()
