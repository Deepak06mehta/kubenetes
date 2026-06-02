from flask import Flask
import redis

app = Flask(__name__)

r = redis.Redis(host='redis-service', port=6379)

@app.route('/vote/<choice>')
def vote(choice):
    r.incr(choice)
    return f"Vote recorded for {choice}"

@app.route('/')
def home():
    return """
    <h1>Vote</h1>
    <a href='/vote/cats'>Cats</a><br>
    <a href='/vote/dogs'>Dogs</a>
    """

app.run(host='0.0.0.0', port=80)