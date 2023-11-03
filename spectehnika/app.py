from flask import Flask

from spectehnika.auth.views import bp as auth_bp

app = Flask(__name__)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run()
