from datetime import datetime
import json
from pytz import timezone

from flask import jsonify


from models import Battle



class dbops():
    def __init__(self):
        self.data="True"

    @staticmethod
    def post_meta(payload):
        print "payload ::", payload

        date = datetime.now()
        my_timezone = timezone('US/Pacific')
        date = my_timezone.localize(date)
        date = date.astimezone(my_timezone)
        print "date is ", date

        battle = Battle(Developer_Issues=payload['Developer_Issues'],
                         Issues_Resolved=payload['Issues_Resolved'],
                         Issues_Pending=payload['Issues_Pending'],
                         Component_Failures=payload['Component_Failures'],
                         Component_Issues=payload['Component_Issues'],
                         Jiras=payload['Jiras']
                        # Date_Updated=date
                       )
        battle.save()

    @staticmethod
    def get_meta():
        mylist = []
        print Battle().to_mongo()
        for data in Battle.objects[:10]:
            mylist.append(json.loads(data.to_json()))
            print data.to_json()
        if mylist is None:
            return jsonify("404 not found")
        return mylist