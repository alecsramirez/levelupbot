from os.path import exists
import pickle

usrdir = "users/"


class User:
    def __init__(self, name, uid, initialBal):
        self.name = name
        self.uid = uid
        self.wallet = initialBal
        self.bank = 0
        self.mcount = 0
        self.levelMessages = True
        self.inv = []
        self.friends = []
        self.quotes = []
        self.data = []


def isUser(uid):
    uid = str(uid)
    return True if exists(usrdir + uid + ".ufl") else False


def loadUser(uid):
    if isUser(uid):
        with open(usrdir + str(uid) + '.ufl', 'rb') as usr:
            return pickle.load(usr)


def saveUser(user: User):
    with open(usrdir + str(user.uid) + '.ufl', 'wb') as usr:
        pickle.dump(user, usr)