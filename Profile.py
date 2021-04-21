from flask import jsonify
from flask_restful import Resource

class Profile(Resource):
    def get(self):
        self.res = jsonify([
            {
                'userid': '00000000001',
                'fullname': 'Saksinkarn Petchkuljinda',
                'picture': 'onhuntoehunhaoe',
                'occupation': 'student',
                'location': 'Chiang Mai',
                'bio': 'ผมมองหาความหลากหลาย และผู้คนมากมาย ถ้าคุณเหงาชวนผมได้ตลอดนะครับ 😄',
                'hosting_event': [
                    {
                        'id':'000000000001',
                        'eventname':'NT Developer Present',
                        'provider':'Pantakan, Saksikarn',
                        'time':'20210830,12:00:00',
                        'tag': ['pitching', 'startup'],
                        'attendee_no': 999999,
                    }, {
                        'id':'000000000002',
                        'eventname':'NT party at Github',
                        'provider':'Pantakan, Saksikarn',
                        'time':'20210830,12:00:00',
                        'tag': ['pitching', 'startup'],
                        'attendee_no': 999999,
                    }
                ],
                'attending_event': [{
                    'id':'000000000001',
                    'eventname':'NT Developer Present',
                    'provider':'Pantakan, Saksikarn',
                    'time':'20210830,12:00:00',
                    'place': 'Suthep, Mueang Chiang Mai District, Chiang Mai',
                    'tag': 'Pitchings',
                }, {
                    'id':'000000000002',
                    'eventname':'NT party at Github',
                    'provider':'Pantakan, Saksikarn',
                    'time':'20210830,12:00:00',
                    'place': 'Suthep, Mueang Chiang Mai District, Chiang Mai',
                    'tag': 'Pitchings',
                },
                ],
            }
        ])

        self.res.headers.add('Access-Control-Allow-Origin', "*")
        self.res.headers.add("Access-Control-Allow-Methods", "GET")
        return self.res
