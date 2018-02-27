
from ..constants import PORT, HOST

import zmq
from control.constants import PORT

def listen(name, callable):

    context = zmq.Context.instance()

    sock = context.socket(zmq.SUB)
    sock.setsockopt(zmq.SUBSCRIBE, b'')
    sock.connect('tcp://%s:%d'%(HOST, PORT))

    def listener(message):
        data = message.decode('ascii')
        callable([int(d) for d in data.split()])
    
    print (callable, "is listening")
    try:
        while True:
        
            message = sock.recv()
            listener(message)
    except Exception as e:
        print (e)
        exit()
