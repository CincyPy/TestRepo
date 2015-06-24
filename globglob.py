import glob
import os

my_path = 'C:/Users/Staff/Desktop/RP/Course materials/Chapter 10/Practice files/images'
possible_files = os.path.join(my_path, "*.gif")

for file_name in glob.glob(possible_files):
    print 'Converting "{}" to JPG...'.format(file_name)
    full_file_name = os.path.join(my_path, file_name)
    new_file_name = full_file_name[0:len(full_file_name)-4]+".jpg"
    os.rename(full_file_name, new_file_name)

could_be_files = os.path.join(my_path, "*/*.png")
for file_name in glob.glob(could_be_files):
    print file_name