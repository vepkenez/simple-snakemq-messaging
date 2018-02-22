from control import listen
from control.constants import REEPLICATOR

def reeplicate(measure_data):
    print ('got a measure:', measure_data)

listen(REEPLICATOR, reeplicate)
