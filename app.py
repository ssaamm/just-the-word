from flask import Flask, render_template
import get_passage

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', passages =
            get_passage.get_passages_for_today())

if __name__ == "__main__":
    app.run(debug = True)
