 
from flask import Flask, request, render_template
import dall_e

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    name = request.form['name']
    image = dall_e.create_image(name)
    return render_template('results.html', image=image)

if __name__ == '__main__':
    app.run()


HTML code for index.html

html
<!DOCTYPE html>
<html>
<head>
  <title>Dall-E Image Generator</title>
</head>
<body>
  <h1>Dall-E Image Generator</h1>
  <form action="/results" method="post">
    <label for="name">Public Figure Name:</label><br>
    <input type="text" id="name" name="name"><br><br>
    <input type="submit" value="Generate Image">
  </form>
</body>
</html>


HTML code for results.html

html
<!DOCTYPE html>
<html>
<head>
  <title>Dall-E Image Generator</title>
</head>
<body>
  <h1>Dall-E Image Generator</h1>
  <img src="{{ image }}">
</body>
</html>
