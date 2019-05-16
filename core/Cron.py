import paramiko
from crontab import CronTab
import conf
import warnings


class CronRun:
    #TODO: clean this up for local and remote cron connections
    def __init__(self):
        if conf.CRON_HOST != 'localhost':
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # TODO: Clean this up.
            warnings.filterwarnings(action='ignore', module='.*paramiko.*')
            self.client.connect(conf.CRON_HOST, 22, conf.CRON_USER, allow_agent=True)
            self.run_cron_remote('notify_delivery.php')

    def run_cron(self, cronname):
        if conf.CRON_HOST == 'localhost':
            return self.run_cron_local(cronname)
        else:
            return self.run_cron_remote(cronname)

    # TODO: get the execution text.
    def run_cron_local(self, cronname):
        if conf.CRON_USER:
            cron = CronTab(conf.CRON_USER)
            cron.new('sudo -u ' + conf.CRON_USER + ' /usr/bin/php ' + conf.CRON_PATH + cronname + ' 2>/dev/null')
            return cron.write()

    def run_cron_remote(self, cron_name):
        data = []
        stdin, stdout, stderr = self.client.exec_command("runcron " + conf.CRON_PATH + cron_name + " accounts:21317")
        for line in stdout:
            data.append(line.strip('\n'))
        self.client.close()
        print(data)
        return data


sshConn = CronRun()
