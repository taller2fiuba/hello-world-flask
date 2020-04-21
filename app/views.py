from app import app

@app.route('/')
def home():
    return 'Hello World of Taller 2!'
