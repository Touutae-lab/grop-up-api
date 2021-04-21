from flask import Flask, request, jsonify
from flask_restful import Api,Resource
from flask_cors import CORS
app=Flask(__name__)
api = Api(app)

from Profile import Profile

class EventData(Resource):
    def get(self):
        self.res = jsonify([{
            'id':'000000000001',
            'eventname':'NT Developer Present',
            'provider':'Pantakan, Saksikarn',
            'time':'20210830,12:00:00',
            'detail':'Presents prototye for Startup thailand',
            'place': 'Suthep, Mueang Chiang Mai District, Chiang Mai',
            'tag': 'Pitchings',
        },
                            {
                                'id':'000000000002',
                                'eventname':'NT party at Github',
                                'provider':'Pantakan, Saksikarn',
                                'time':'20210830,12:00:00',
                                'detail':'Party with milk and mashmellos',
                                'place': 'Suthep, Mueang Chiang Mai District, Chiang Mai',
                                'tag': 'Pitchings',
                            },
                            {
                                'id':'000000000003',
                                'eventname':'NT Developer Present',
                                'provider':'Pantakan, Saksikarn',
                                'time':'20210830,12:00:00',
                                'detail':'Presents prototye for Startup thailand',
                                'place': 'Suthep, Mueang Chiang Mai District, Chiang Mai',
                                'tag': 'Pitchings',
                            },
                            {
                                'id':'000000000004',
                                'eventname':'NT Developer Present',
                                'provider':'Pantakan, Saksikarn',
                                'time':'20210830,12:00:00',
                                'detail':'Presents prototye for Startup thailand',
                                'place': 'Suthep, Mueang Chiang Mai District, Chiang Mai',
                                'tag': 'Pitchings',
                            },
                            ])
        self.res.headers.add('Access-Control-Allow-Origin', "*")
        self.res.headers.add("Access-Control-Allow-Methods", "GET")
        return self.res

api.add_resource(EventData,"/event")
api.add_resource(Profile, "/profile")

if __name__ == "__main__":
    app.run(host='192.168.1.42', port='5000', debug=True) # Change IP to your pc IP
