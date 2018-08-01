import telnetlib
import datetime

#HOST = "172.30.157.144"
#user = "root"
#password = "root"

class Telnet:

    def __init__(self):
        print('Show run collecting...')

    def test_method(self, val1, HOST, user, password):

        tn = telnetlib.Telnet(HOST)
        tn.read_until("Username:")
        tn.write(user + "\n")

        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")


            tn.write("ter len 0\n")
            tn.write("show run\n")
            tn.write("exit\n")

        date = datetime.datetime.today()
        time = str(date.strftime("%Y-%m-%d_%H:%M:%S"))
        filename = 'currentconfig.txt'
        f_obj = open(filename, 'w')
        string = tn.read_all()
        f_obj.write(string)
        f_obj.close()
        return filename
        
