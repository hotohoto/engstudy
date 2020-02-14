from engstudy.server import app


@app.route("/")
def index():
    return "EngStudy backend server is running."
