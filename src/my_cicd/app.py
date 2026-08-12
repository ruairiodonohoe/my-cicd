"""Application module description."""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home() -> str:
    """Home function."""
    return "Home again"


if __name__ == "main":  # pragma: no cover
    app.run()
