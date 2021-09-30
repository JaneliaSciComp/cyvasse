#! /usr/bin/python3

#import sys
import os
import shutil

source_file_path = "bad-avis-read-only/SC030_100519_side_face_4-0000.avi"
target_folder_path = 'many-copies-of-bad-avi-read-only'

source_file_name = os.path.basename(source_file_path)
source_base_name = os.path.splitext(source_file_name)[0]

for i in range(500):
    target_file_name = "%s-%03d.avi" % (source_base_name,i)
    target_file_path = os.path.join(target_folder_path, target_file_name)
    shutil.copyfile(source_file_path, target_file_path)
