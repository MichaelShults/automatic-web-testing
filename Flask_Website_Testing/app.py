from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    results = []
    if request.method == 'POST':
        query = request.form.get('q', '').strip().lower()
        if query == 'dog':
            results = ["DOG 1", "DOG 2", "DOG 3"]
    return render_template('index.html', results=results)




if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)