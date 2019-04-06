
from flask import Flask, Blueprint
from flask_restplus import Api
from statusCheck import apiStatus, nsCheck
from redisConnection.redis import apiRedis, nsRedis


app = Flask(__name__)

##API-test
blueprint = Blueprint('api-test', __name__, url_prefix='/api-test')
apiStatus.init_app(blueprint)
apiStatus.add_namespace(nsCheck)
app.register_blueprint(blueprint)

##API-redis
blueprint2 = Blueprint('api-redis', __name__, url_prefix='/api-redis')
apiRedis.init_app(blueprint2)
apiRedis.add_namespace(nsRedis)
app.register_blueprint(blueprint2)


@app.route("/")
def hello():
    return "Hello World !"



if __name__ == "__main__":
    app.run()