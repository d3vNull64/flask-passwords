from flask import Flask

from routes import generator_bp, index_bp

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(index_bp)
app.register_blueprint(generator_bp)

app.config.from_pyfile("config.py")

if __name__ == "__main__":
    app.run(debug=True)
