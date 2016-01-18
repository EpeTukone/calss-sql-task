import json
import datetime


GOLD = 'Gold'
SILVER = 'Silver'
###### database ######
Log_pass = {'mail.@tut.by': '12WW34e', 'moder@mail.ru': '1234', 'adminko@gmail.com': 'A1234'}
Progress_dict = {1: "super pihar'", 2: "geniy randoma"}
session = None

class Player(object):

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name
        self.session = []
        self.wallet = {}
        self.progress = {}
        self.session_id = 0   # counter of session
        self.type = 1         # 1 - player, 2 - moderator, 3 - administrator
        self.ban_status = 0   # 0 - player isn't banned, 1 - player is banned
        self.mute = 0         # 0 - player's chat and microphone isn't off, 1 - player's chat and micro is off


    def log_in(self, email, password):
        global session
        if email not in Log_pass:
            result = 'wrong email'
        if email in Log_pass:
            if Log_pass.get(email) != password:
                result = 'wrong password'
            if Log_pass.get(email) == password and self.session_id == 0:
                result = 'authentication is successful'
                self.session_id += 1
                session = Session(self.session_id)
                temp = {self.session_id: [str(session.start()), None]}
                self.session.append(temp)
            elif Log_pass.get(email) == password and self.session_id != 0 and \
                            (self.session[self.session_id - 1]).get(self.session_id)[1] != None:
                result = 'authentication is successful'
                self.session_id += 1
                session = Session(self.session_id)
                temp = {self.session_id: [str(session.start()), None]}
                self.session.append(temp)
            elif Log_pass.get(email) == password and self.session_id != 0 and\
                            (self.session[self.session_id - 1]).get(self.session_id)[1] == None:
                result = 'authentication has already been done\nauthentication failed'
        return result


    def log_out(self, email):
        global session
        (self.session[self.session_id - 1]).get(self.session_id)[1] = str(session.stop())
        result = 'log out has done'
        return result


    def init_money(self):
        money_gold = Money(GOLD, 100)
        quantity_gold = money_gold.as_dict()
        money_silver = Money(SILVER, 100)
        quantity_silver = money_silver.as_dict()
        self.wallet = {GOLD: quantity_gold.get(GOLD),
                       SILVER: quantity_silver.get(SILVER)}


    def money_add(self, name_of_money, quantity):
        if name_of_money == GOLD:
            quantity_money = self.wallet.get(GOLD) + quantity
            self.wallet[GOLD] = quantity_money
        if name_of_money == SILVER:
            quantity_money = self.wallet.get(SILVER) + quantity
            self.wallet[SILVER] = quantity_money


    def money_remove(self, name_of_money, quantity):
        if name_of_money == GOLD:
            quantity_money = self.wallet.get(GOLD) - quantity
            self.wallet[GOLD] = quantity_money
        if name_of_money == SILVER:
            quantity_money = self.wallet.get(SILVER) - quantity
            self.wallet[SILVER] = quantity_money


    def add_progress(self, name_of_progress):
        new_progress = Progress(name_of_progress)
        self.progress[len(self.progress) + 1] = [name_of_progress, new_progress.date()]


    def as_dict(self):
        dict_ = {
            'email': self.email,
            'password': self.password,
            'name': self.name,
            'account type': self.type,
            'ban status': self.ban_status,
            'mute status': self.mute,
            'wallet': self.wallet,
            'session': self.session
        }
        return dict_


    def save(self, file_object):
        json.dump(self.as_dict(), file_object)


    def __str__(self):
        format_str = 'email= "{}", password= "{}", name= "{}",\naccount type= "{}", ban status= "{}",' \
                     ' mute status= "{}",\nwallet= "{}",\nprogress= {}\nsession= "{}"'
        return format_str.format(self.email, self.password, self.name, self.type,
                                 self.ban_status, self.mute, self.wallet, self.progress, self.session)





class Session(object):
    def __init__(self, session_id):
        self.session_id = session_id
        self.start_time = None
        self.finish_time = None


    def start(self):
        self.start_time = datetime.datetime.now()
        return self.start_time


    def stop(self):
        self.finish_time = datetime.datetime.now()
        return self.finish_time





class Money(object):
    def __init__(self, name_of_money, quantity):
        self.name_of_money = name_of_money
        self.quantity = quantity


    def as_dict(self):
        dict_ = {
            str(self.name_of_money): self.quantity
        }
        return dict_



class Progress(object):
    def __init__(self, name):
        self.name = name
        self.date_created = None


    def date(self):
        self.date_created = str(datetime.datetime.now())
        return self.date_created






if __name__ == "__main__":

####### create a new player ######
    player = Player('mail.@tut.by', '12WW34e', 'drednout')
    print 'Create new player:\n', player, '\n',\
    '-----------------------------------------------------------------------'

###### authentication ######
    print 'authentication:\n', player.log_in('mail.@tut.by', '12WW34e'), '\n', player, '\n',\
    '-----------------------------------------------------------------------'

###### add money for a player with new account ######
    player.init_money()
    print 'Add money for a player with new account:\n', player, '\n',\
    '-----------------------------------------------------------------------'

###### add money to player ######
    player.money_add(GOLD, 200)
    player.money_add(SILVER, 2000)
    print 'Add money to player:\n', player, '\n',\
    '-----------------------------------------------------------------------'

###### remove money from player ######
    player.money_remove(GOLD, 50)
    player.money_remove(SILVER, 500)
    print 'Remove money from player:\n', player, '\n',\
    '-----------------------------------------------------------------------'

###### add a progress ######
    player.add_progress(Progress_dict.get(1))
    player.add_progress(Progress_dict.get(2))
    print 'add a progress:\n', player, '\n',\
    '-----------------------------------------------------------------------'

###### authentication number two ######
    print 'authentication number two:\n', player.log_in('mail.@tut.by', '12WW34e'), '\n', player, '\n',\
    '-----------------------------------------------------------------------'

###### log out ######
    print 'log out:\n', player.log_out('mail.@tut.by'), '\n', player, '\n',\
    '-----------------------------------------------------------------------'

###### save json.dump ######
    name_of_player = player.as_dict().get('name')
    player.save(open(str(name_of_player + '.txt'), 'w'))
    print 'save json.dump:\niformation was save into', (name_of_player + '.txt'), '\n',\
    '-----------------------------------------------------------------------'

###### authentication number two, try again ######
    print 'authentication number two:\n', player.log_in('mail.@tut.by', '12WW34e'), '\n', player, '\n',\
    '-----------------------------------------------------------------------'

