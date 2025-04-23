from flask import Flask

from routes import generator_bp, index_bp

app = Flask(__name__)
app.register_blueprint(index_bp)
app.register_blueprint(generator_bp)

if __name__ == "__main__":
    app.run(debug=True)
