from flask import Flask

app = Flask(__name__)

def generate_html_from_dataframe(df):
    html = "<h1>Student Data</h1>"
    html += df.to_html(index=False)
    return html

@app.route('/')
def index():
    return "Florian POSEZ 22320180"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)