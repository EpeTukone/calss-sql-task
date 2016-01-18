import json
import datetime
import MySQLdb


GOLD = 'Gold'
SILVER = 'Silver'


class Player(object):

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name
        self.session = []
        self.wallet = {}
        self.type_account = 1
        self.mute_status = 0
        self.ban_status = 0


    def load_to_db(self,):
        dict_ = {
        'email': str(self.email),
        'password': str(self.password),
        'name': str(self.name),
        'type_account': self.type_account,
        'mute_status': self.mute_status,
        'ban_status': self.ban_status
        }
        # sql_query = """UPDATE player SET email=%(email); UPDATE player SET name=%(name)s;
        #  UPDATE player SET password=%(password); UPDATE player SET type_account=%(type_account);
        #  UPDATE player mute_status=%(mute_status); UPDATE player ban_status=$(ban_status)"""
        sql_query = """INSERT INTO `player` (`email`, `password`, `name`, `type_account`, `mute_status`, `ban_status`)
            VALUES (email=%(email)s, password=%(password)s, name=%(name)s,
            type_account=%(type_account)s, mute_status=%(mute_status)s, ban_status=%(ban_status)s);
        """
        with con:
            cur = con.cursor()
            cur.execute(sql_query, dict_)
        result = "load to db successful"
        return result

    def __str__(self):
        format_str = 'email= "{}", password= "{}", name= "{}",\n' \
                     'type_account= "{}", mute_status= "{}", ban_status = {}'
        return format_str.format(self.email, self.password, self.name,
                                 self.type_account, self.mute_status, self.ban_status )

if __name__ == "__main__":
    con = MySQLdb.connect('localhost', 'root', 'mysql', 'players')
####### create a new player ######
    player = Player('mail.@tut.by', '12WW34e', 'drednout')
    print 'Create new player:\n', player, '\n',\
    player.load_to_db()
    '-----------------------------------------------------------------------'



#delete FROM players.player
#where id_player = 3