import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/media/aayush/New Volume/IGVC_assignment/install/assignment_1'
