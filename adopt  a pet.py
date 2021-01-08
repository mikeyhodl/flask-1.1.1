from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return '''
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
<ul>
    <li>Dog</li>
    <li>Cats</li>
    <li>Rabits</li>
</ul>
  '''

@app.route('/animals/<pet_type>')
def animals(pet_type):
    html = '<h1>List of pets</h1>'
    return html;

  
