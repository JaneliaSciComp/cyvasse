#! /usr/bin/python3

import os
import shutil

if os.path.exists('many-copies-of-bad-avi'):
    shutil.rmtree('many-copies-of-bad-avi')
shutil.copytree('many-copies-of-bad-avi-read-only', 'many-copies-of-bad-avi')

if os.path.exists('many-copies-of-bad-avi-output'):
    shutil.rmtree('many-copies-of-bad-avi-output')
os.mkdir('many-copies-of-bad-avi-output')

os.system('python3 cyvasse.py many-copies-of-bad-avi many-copies-of-bad-avi-output')
