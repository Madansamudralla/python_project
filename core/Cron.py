import paramiko
from crontab import CronTab
import array
from core.config import getConfig


class CronRun:
    def __init__(self):
        if getConfig("CRON_HOST") != 'localhost':
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(getConfig("CRON_HOST"), 22, self.getConfig("USER"), self.getConfig('key'))

    def runcron(self, cronname):
        if getConfig("CRON_HOST") == 'localhost':
            return self.runcronlocal(cronname)
        else:
            return self.runcronremote(cronname)

    def runcronlocal(self, cronname):
        sudo = ''
        if getConfig('CRON_USER'):
            cron = CronTab(getConfig('CRON_USER'))
            job = cron.new('sudo -u ' + getConfig('CRON_USER') + ' /usr/bin/php ' + getConfig(
                'CRON_PATH') + cronname + ' 2>/dev/null')
            return cron.write()

    def runcronremote(self, cronname):
        data = array.array()
        stdin, stdout, stderr = self.client.exec_command("runcron " + getConfig('CRON_PATH') + cronname)
        for line in stdout:
            data.append(line.strip('\n'))
        self.client.close()
        return data
