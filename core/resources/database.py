from core.runtime import connection_manager
from core.resources.resource import GenericResource

from core.lib.database import DbConnection


class Database(GenericResource):
    """Database resource class is meant to represent a typical Unix/Linux resource.
    The following attributes are mandatory and must be passed via the testbed YAML file.

    attributes:
        :ip: IP Address of the device
        :user: Username
    """
    def bootstrap(self):
        """This method is used to establish the SSH connection to the device and fill up useful metadata related to
        the device.

        """

        self.db = connection_manager.get(DbConnection, host=self.ip, port=3306, user=self.user, password=self.password)

        self.connected = True

