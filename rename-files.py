#!/usr/bin/env python
import os
import re

current_dir = os.getcwd()

# ex: 12345-myfile.pdf
pattern = re.compile(r'(\d{3,})-(.*\.pdf)')

for file in os.listdir(current_dir):
    match = pattern.match(file)
    if match:
        old_name = match.group(0)
        new_name = match.group(2)
        print('renaming %s to %s ' % (old_name, new_name))

        # if file not exists
        if not os.path.isfile(new_name):
            os.rename(old_name, new_name)
        else:
            print('%s exists' % (new_name))
