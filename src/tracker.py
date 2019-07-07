'''
Author: David Porfirio
'''

import time
import datetime
import _thread as thread
from reader import *

class Tracker:

    '''
    Class: ChoreScreen
    Purpose: Contains and updates the chore data. Also controls access to the
        chore data.
    '''

    def __init__(self, filename):
        reader = Reader()
        self.data = reader.read(filename)

        # begin listening for day changes
        thread.start_new_thread(self.listen_for_day_change, ("thread_timer",))

    def listen_for_day_change(self, name):

        '''
        Method: listen_for_day_change
        Purpose: listen for a new day and initiate the updating of the chore
            objects
        '''

        old_day = datetime.datetime.now().day
        while True:
            time.sleep(5)
            now_day = datetime.datetime.now().day
            is_new_day = (now_day != old_day)
            old_day = now_day
