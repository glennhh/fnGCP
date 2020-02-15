#!/usr/bin/env python
##############################################
#   ENV: ubuntu 16.04
#   Python 2.7
##############################################

import sys
import os
import re
import pymysql
import time
from numpy.random import rand
from datetime import datetime

startT = datetime.now()
#print(startT)
os.popen('gcloud functions deploy hello --runtime python37 --trigger-http --allow-unauthenticated --max-instances 1 --timeout 60 --project startup-262316 --region us-east1 --memory 256')
endT = datetime.now()
#print(endT)
latCold = (endT - startT).total_seconds()
print('cold latency is: %f' % latCold)

startT = datetime.now()
#print(startT)
os.popen('gcloud functions call hello --project startup-262316 --region us-east1')
endT = datetime.now()
#print(endT)
latCold = (endT - startT).total_seconds()
print('warm latency is: %f' % latCold)
