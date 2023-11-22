import config
import os
from flask import redirect

connex_app = config.connex_app

connex_app.add_api("swagger.yml")

@connex_app.route("/")
def home():
    return redirect("/api/ui")

if __name__ == "__main__":
    connex_app.run(host='0.0.0.0', port=int(os.getenv("PORT", default="8000")))