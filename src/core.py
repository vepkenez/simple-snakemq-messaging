
from ..constants import PORT, HOST

import zmq
from control.constants import PORT

import sys
import os


def is_only_num_and_spaces(number_sequence):
    return all(var.isdigit() for var in number_sequence.split())

def listen(name, callable):

    context = zmq.Context.instance()

    sock = context.socket(zmq.SUB)
    sock.setsockopt(zmq.SUBSCRIBE, b'')
    sock.connect('tcp://%s:%d'%(HOST, PORT))

    def listener(message):
        data = message.decode('ascii')
        if is_only_num_and_spaces( data ):
            callable([int(d) for d in data.split()])
        else:
            callable( data )
    
    print (callable, "is listening")
    #try:
    while True:
    
        message = sock.recv()
        listener(message)
    # except Exception as e:
    #     exc_type, exc_obj, exc_tb = sys.exc_info()
    #     fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #     print(exc_type, fname, exc_tb.tb_lineno)
    #     exit()
