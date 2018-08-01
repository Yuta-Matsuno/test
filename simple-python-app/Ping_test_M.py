import telnetlib
import datetime

class Telnet:

    def __init__(self):
        print('Alive monitoring...')

    def test_method(self, val1 , Target, HOST, user, password):

        tn = telnetlib.Telnet(HOST)
        tn.read_until("Username:")
        tn.write(user + "\n")

        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")

        print("Ping target is " + Target)
        tn.write("ter len 0\n")
        tn.write("ping " + Target + "\n")

        result = tn.expect(["!!!!!"], 3)[0]
        if result == -1: #NG pattern
            print('!!!Ping NG!!!')
        else: #OK pattern
            print('[Ping OK]')
        tn.write("exit\n")
        
