#!/usr/bin/env python3

from time import sleep
from rignetctl import RigNetCtl

def main():
    r = RigNetCtl()
    r.connect()

    print("Creating while")
    while True:
        freq = r.get_frequency()
        mode = r.get_mode().splitlines()[0]
        print("Mode:{}\tFreq: {}".format(mode, freq))
        sleep(1)

if __name__ == "__main__":
    main()