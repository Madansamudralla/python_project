
# Testing sandbox
MY_HOST_NAME = "sandbox86"

# Cron running configuration
CRON_SANDBOX = "sandbox86"

# DB connection settings

DATABASE = {
    "AUTOMATION": {
        'host': 'mysqldev.avangate.local',
        'dbname': 'automation',
        'user': 'automation',
        'password': 'withc--',
        'port': 3306
    },
    "DEVELOPER": {
        'host': 'mysqldev.avangate.local',
        'dbname': 'avangate',
        'user': 'devel',
        'pass': 'withc--',
        'port': 3306
    }
}
