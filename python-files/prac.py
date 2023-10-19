
import os
import sys

script_path = __file__

print  ('script full path is', script_path, sep=': ')

print ('script is in %s correct?' % script_path)

script_name = os.path.split(__file__)[1]
print("Script Name:", script_name)

print ('\n\n')

the_string = 'dsdsa dsa dsad sa dsa'

try:
    count = 0
    while (the_string[count]):
        count +=1
except:
    print ('Found the length ... ', count)

