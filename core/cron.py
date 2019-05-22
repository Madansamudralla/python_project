import paramiko
import config_automation
import warnings


class CronRun:

    def __init__(self):
        if config_automation.Config.CRON_HOST != 'localhost':
            try:
                self.client = paramiko.SSHClient()
                self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                warnings.filterwarnings(action='ignore', module='.*paramiko.*')
                self.client.connect(config_automation.Config.CRON_HOST, 22, config_automation.Config.CRON_USER,
                                    allow_agent=True)
            except paramiko.AuthenticationException:
                raise ConnectionError('Could not connect via SSH Client Make sure you have the proper user in the '
                                      '"config_automation.py" file and that your SSH agent is opened.')

    def run_cron(self, cron_name):
        if config_automation.Config.CRON_HOST == 'localhost':
            return self.run_cron_local(cron_name)
        else:
            return self.run_cron_remote(cron_name)

    # TODO: Clean debugging prints after core is implemented

    def run_cron_local(self, cron_name):
        data = []
        try:
            if config_automation.Config.CRON_USER:
                stdin, stdout, stderr = self.client.exec_command('sudo -u ' + config_automation.Config.CRON_USER
                                                                 + ' /usr/bin/php ' + config_automation.Config.CRON_PATH
                                                                 + cron_name + ' 2>/dev/null')
                for line in stdout:
                    data.append(line.strip('\n'))
        finally:
            self.client.close()
            print(data)
        return data

    # TODO: Clean debugging prints after core is implemented

    def run_cron_remote(self, cron_name):
        data = []
        try:
            stdin, stdout, stderr = self.client.exec_command("runcron " +
                                                             config_automation.Config.CRON_PATH + cron_name)
            for line in stdout:
                data.append(line.strip('\n'))
        finally:
            self.client.close()
            print(data)
        return data

