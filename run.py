# Local application imports
from content import app

# Third party imports

# Standard library import
import os


if __name__ == "__main__":
    app.secret_key = os.urandom(255)
    app.run(port=4000, debug=False)