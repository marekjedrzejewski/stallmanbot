#!/usr/bin/python3

import sys
import time
import re
from matrix_client.client import MatrixClient

if len(sys.argv) != 4:
    print("USAGE: ./pastabot.py username password room")
    sys.exit(1)

USERNAME = sys.argv[1]
PASSWORD = sys.argv[2]
ROOMNAME = sys.argv[3]

keys_and_responses = {
    r'(?<!gnu[+/])linu(x|ks)':
    """
    I'd just like to interject for moment. What you're refering to as Linux, is in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX.

    Many computer users run a modified version of the GNU system every day, without realizing it. Through a peculiar turn of events, the version of GNU which is widely used today is often called Linux, and many of its users are not aware that it is basically the GNU system, developed by the GNU Project.

    There really is a Linux, and these people are using it, but it is just a part of the system they use. Linux is the kernel: the program in the system that allocates the machine's resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added, or GNU/Linux. All the so-called Linux distributions are really distributions of GNU/Linux!
    """,

}


class PastaBot():
    def __init__(self, username, password, roomname):
        # connect to room
        self.client = MatrixClient("http://matrix.org")
        self.token = self.client.login_with_password(username=username,
                                                     password=password)
        self.room = self.client.join_room(roomname)

        # add bot reactions
        self.room.add_listener(self.on_message)
        self.client.start_listener_thread()

    def default_response(self, message):
        return self.crypto.analyze_message_and_prepare_response(message)

    def on_message(self, room, event):
        if event['type'] == "m.room.message":
            if USERNAME in event['sender']:
                return
            if event['content']['msgtype'] == "m.text":
                message = event['content']['body']
                for key in keys_and_responses:
                    if re.search(key, message, re.I):
                        self.room.send_text(keys_and_responses[key])


PastaBot(USERNAME, PASSWORD, ROOMNAME)
while True:
    time.sleep(1)
