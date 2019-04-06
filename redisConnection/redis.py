import redis
from flask_restplus import Resource
from flask_restplus import Api
from flask import make_response, session, jsonify,request

apiRedis = Api(version='1.0', title='API status check',description='Beta version of docker API')
nsRedis= apiRedis.namespace('default', description='Operations related to connection')

@nsRedis.route('/writeToRedis')
@apiRedis.doc(params={'variable': 'variable name', 'value':'value to set to the variable'})
class redisWrite(Resource):
    def get(self):
        variable = request.args.get('variable', type=str)
        value = request.args.get('value', type=str)
        writeVariableToRedis(variable,value,host="redis-server")

@nsRedis.route('/readRedis')
@apiRedis.doc(params={'variable': 'variable name'})
class redisRead(Resource):
    def get(self):
        variable = request.args.get('variable', type=str)
        return jsonify({"value" : getVariableFromRedis(variable,host="redis-server").decode("utf-8")})

##By default, redis run  on port 6379
## For this code to work in dev, you need to start a redis server
## In a command line, type "redis-server"
## to stop a redis server on mac => redis-cli shutdown

## if redis runs in a docker container, change the port, corresponding to your port mapping machine<->container

# If this flask app is in a docker container itself => need to use docker compose to make them communicate
#declare redis-server in the docker-compose
#then in flask replace localhost by redis-server to target the redis server
#both containers will communicate

def writeVariableToRedis(name,value,host="localhost",port=6379):
    r = redis.Redis(host=host, port=port, db=0)
    r.set(name, value)

def getVariableFromRedis(name,host="localhost",port=6379):
    r = redis.Redis(host=host, port=port, db=0)
    return r.get(name)
