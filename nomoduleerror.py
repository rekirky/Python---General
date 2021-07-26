import os
import subprocess
import sys


subprocess.run([sys.executable, '-m', 'pip', 'install', 'tensorflow'])
subprocess.run([sys.executable, '-m', 'pip', 'install', 'imutils'])

sys.path.append('my/path/to/module/folder')


from tensorflow.keras.models import load_model
from imutils.contours import sort_contours
from matplotlib import pyplot as plt