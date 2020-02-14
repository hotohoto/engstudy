from engstudy.server import app


@app.route("/login")
def login():
    return "trying to login"
