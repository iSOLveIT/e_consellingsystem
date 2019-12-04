# Local application imports
from content import app, mysql

# Third party imports
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

# Standard library import


class TokenGEN:
    @staticmethod
    def get_reset_token(user_id, expire_secs=3600):
        s = Serializer(app.config['SECRET_KEY'], expire_secs)
        token = s.dumps({'uid': user_id}).decode('utf-8')
        return token

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        cur = mysql.connection.cursor()
        
        try:
            user_id = s.loads(token)['uid']
            pkey = int(user_id)
        except:
            return None
        query = "SELECT * FROM user WHERE user_id=%s"
        result = cur.execute(query, [pkey])
        if result > 0:
            data = cur.fetchone()
            #close db
            cur.close()
            return data
            
