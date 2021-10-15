import subprocess
import optparse



class Forensic:
    def __init__(self):
        self._key = None
        self._args = None
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, keyInput):
        self._key = int(keyInput)


    def module_checker(self):
        argument = self._key
        switcher = {
        1 : "os_users",
        2 : "passwd_history",
        3 : "selected_process",
        4 : "running_process",
        5 : "process_detail",
        6 : "service_detail",
        7 : "interface_detail",
        8 : "host_detail",
        9 : "route_detail",
        10 : "listen_port",
        11 : "listen_process",
        }
        return switcher.get(argument, "nothing")


    def os_users(self):
        subprocess.call(['awk', '{print $1}', '/etc/passwd'])

    def passwd_history(self):
        user = input('username\n')
        subprocess.call(['passwd', '-S', user])

    def selected_process(self):
        process = input('process\n')
        subprocess.call("ps aux | grep " + process, shell=True)

    def running_process(self):
        subprocess.call(['top'])

    def process_detail(self):
        process_id = (input("process ID\n"))
        subprocess.call(['lsof', '-p', process_id])

    def service_detail(self):
        service_name = (input("service name\n"))
        subprocess.call(['systemctl', 'status', service_name])

    def interface_detail(self):
        interface_name = (input("interface name\n"))
        subprocess.call(['ifconfig', interface_name])

    def host_detail(self):
        subprocess.call(['cat', '/etc/hosts'])

    def route_detail(self):
        subprocess.call(['iptables', '-L', '-n'])

    def listen_port(self):
        subprocess.call(['lsof', '-i'])


    def listen_process(self):
        subprocess.call(['netstat', '-nap'])


if __name__ == "__main__":
    handeler = Forensic()
    handeler.key = input('select your modules\n1 : os users\n2 : password History\n3 : selected process\n4 : running process\n5 : process detail\n6 : service detail\n7 : interface detail\n8 : hosts detail\n9 : routes detail\n10 : listening port\n11 : listening process\n')
    if handeler.module_checker() == "os_users":
        handeler.os_users()
    if handeler.module_checker() == "passwd_history":
        handeler.passwd_history()
    if handeler.module_checker() == "selected_process":
        handeler.selected_process()
    if handeler.module_checker() == "running_process":
        handeler.running_process()
    if handeler.module_checker() == "process_detail":
        handeler.process_detail()
    if handeler.module_checker() == "service_detail":
        handeler.service_detail()
    if handeler.module_checker() == "host_detail":
        handeler.host_detail()
    if handeler.module_checker() == "interface_detail":
        handeler.interface_detail()
    if handeler.module_checker() == "route_detail":
        handeler.route_detail()
    if handeler.module_checker() == "listen_port":
        handeler.listen_port()
    if handeler.module_checker() == "listen_process":
        handeler.listen_process()
