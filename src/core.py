import snakemq.link
import snakemq.packeter
import snakemq.messaging
import snakemq.message

Message = snakemq.message.Message

from .constants import PORT, HOST

def connect(name):
    link = snakemq.link.Link()
    packeter = snakemq.packeter.Packeter(link)
    messaging = snakemq.messaging.Messaging(name, "", packeter)
    link.add_connector((HOST, PORT))

    return link, messaging, Message


def listen(name, callable):

    link, messaging, Message = connect(name)
    link.add_listener(("", PORT))

    def listener(conn, ident, message):

        data = message.data.decode('ascii')
        callable([int(d) for d in data.split()])

    messaging.on_message_recv.add(listener)
    print (callable, "is listening")
    link.loop()

