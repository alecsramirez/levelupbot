from os.path import exists

usrdir = "users/"

def isUser(uid):
    uid = str(uid)
    return True if exists(usrdir + uid + ".ufl") else False