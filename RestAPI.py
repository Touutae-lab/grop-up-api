from flask import Flask
from flask_restful import Api,Resource

app=Flask(__name__)
api = Api(app)

class EventData(Resource):
    def get(self):
        return [{
            'id':'000000000001',
            'eventname':'NT Developer Present',
            'provider':'Pantakan, Saksikarn',
            'time':'2021/08/30,12:00:00',
            'img': './mnt/f/grop-up/grop-up-api/pictures',
            'detail':'Presents prototye for Startup thailand',
            'place': 'Suthep, Mueang Chiang Mai District, Chiang Mai',
            'tag': 'Pitchings/Dev',
        },
        {
            'id':'000000000002',
            'eventname':'NT party at Github',
            'provider':'Pantakan, Saksikarn',
            'time':'2021/08/30,12:00:00',
            'img': './mnt/f/grop-up/grop-up-api/pictures',
            'detail':'Party with milk and mashmellos',
            'place': 'Suthep, Mueang Chiang Mai District, Chiang Mai',
            'tag': 'Pitchings/Dev',
        },
        {
            'id':'000000000003',
            'eventname':'NT Developer Present',
            'provider':'Pantakan, Saksikarn',
            'time':'2021/08/30,12:00:00',
            'img': './mnt/f/grop-up/grop-up-api/pictures',
            'detail':'Presents prototye for Startup thailand',
            'place': 'Suthep, Mueang Chiang Mai District, Chiang Mai',
            'tag': 'Pitchings/Dev',
        },
        {
            'id':'000000000004',
            'eventname':'NT Developer Present',
            'provider':'Pantakan, Saksikarn',
            'time':'2021/08/30,12:00:00',
            'img': './mnt/f/grop-up/grop-up-api/pictures',
            'detail':'Presents prototye for Startup thailand',
            'place': 'Suthep, Mueang Chiang Mai District, Chiang Mai',
            'tag': 'Pitchings/Dev',
        },
    ]


api.add_resource(EventData,"/event")

if __name__ == "__main__":
    app.run(debug=True)
