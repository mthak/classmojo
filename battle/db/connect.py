from models import Battle

'''  moved to init 
connect(
    Config.DATABASE_NAME,
    host=Config.DATABASE_HOST,
    port=Config.DATABASE_PORT
)
'''

def post_meta(payload):
    print "payload ::", payload
    battle = Battle(Developer_Issues=payload['Developer_Issues'],
                     Issues_Resolved=payload['Issues_Resolved'],
                     Issues_Pending=payload['Issues_Pending'],
                     Component_Failures=payload['Component_Failures'],
                     Component_Issues=payload['Component_Issues'],
                     Jiras=payload['Jiras']
                   )
    battle.save()


def get_meta(data):
    return  True