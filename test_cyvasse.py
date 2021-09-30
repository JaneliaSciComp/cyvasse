#! /usr/bin/python3

import os
import shutil

if os.path.exists('cyvasse-drop'):
    shutil.rmtree('cyvasse-drop')
shutil.copytree('cyvasse-drop-read-only', 'cyvasse-drop')

if os.path.exists('cyvasse-drop-output'):
    shutil.rmtree('cyvasse-drop-output')
os.mkdir('cyvasse-drop-output')

os.system('python3 cyvasse.py cyvasse-drop cyvasse-drop-output')
