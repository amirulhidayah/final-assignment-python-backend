import config
from flask import redirect

connex_app = config.connex_app

connex_app.add_api("swagger.yml")

@connex_app.route("/")
def home():
    return redirect("/api/ui")

if __name__ == "__main__":
    connex_app.run()