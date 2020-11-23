#!c:\ecommerce\ecom_env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'startapp==0.1.6.5','console_scripts','startapp'
__requires__ = 'startapp==0.1.6.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('startapp==0.1.6.5', 'console_scripts', 'startapp')()
    )
