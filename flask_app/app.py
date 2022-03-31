from flask_app import create_app
from flask_app.config import DevelopmentConfig

flask_app = create_app(DevelopmentConfig)
flask_app.config["ENV"] = "development"
flask_app.config["DEBUG"] = True
flask_app.config["TESTING"] = True

from werkzeug.debug import (
    DebuggedApplication,
)  # Workaround, problems enabling debug on VSCode

flask = DebuggedApplication(flask_app, True)

if __name__ == "__main__":
    flask.run(debug=True)
