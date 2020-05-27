#!"D:\User\Desktop\Python Projects_SoftUni\Python-OOP\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'pokemon==0.35','console_scripts','pokemon'
__requires__ = 'pokemon==0.35'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pokemon==0.35', 'console_scripts', 'pokemon')()
    )
