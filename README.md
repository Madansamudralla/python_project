autmation.behave: Python Automation Framework - 2Checkout
==============================================================================

`behave`_ is a BDD test framework and cucumber-clone for Python.
It should extend the excellent documentation of `behave`_.

SEE ALSO:
  * https://github.com/behave/behave.example
  * behave:  http://pypi.python.org/pypi/behave/

DOCUMENTATION:
  * http://behave.github.com/behave.example (latest version)
  * https://docs.paramiko.org
  * https://2.python-requests.org/en/master/
  * http://docs.peewee-orm.com/en/latest/


REPOSITORIES:
  * https://github.com/behave/behave
  * https://github.com/SeleniumHQ/selenium
  * https://github.com/paramiko/paramiko
  * https://github.com/kennethreitz/requests
  * https://github.com/coleifer/peewee


INSTALL
------------------------------------------------------------------------------

To prepare the local installation, use the following command to install
all prerequisites::

    pip install -r requirements.txt



HOWTO
------------------------------------------------------------------------------

Run `selenium`_ local::
    
    java - jar [selenium_version]

Run `behave`_ tests::

    behave --tags @all -f json.pretty -o tmp/jenkins/behave_json.json
    python convert2cucumber.py tmp/jenkins/behave_json.json

