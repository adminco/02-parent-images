#!/usr/bin/python3

import sys,os,re

#Working directory argument
directory = sys.argv[1]

#Regex to get base image
base_regex = re.compile(r'''(
(FROM)      #This is to match the 'FROM' before the base image
\s          #This is to match any space, tab or newline character before the base image
(.*)        #This is to match the base image
)''',re.VERBOSE)

#Traverse directory recursively and print any detected Dockerfile in "<FILE PATH>: <PARENTIMAGE>" format
for folders, subfolders, files in os.walk(directory):
    for file in files:
        if file == "Dockerfile":
            path_to_file = folders + "/" + file            
            file_content = open(path_to_file, 'r')
            base_image = base_regex.search(file_content.read())
            print (path_to_file + ":" + " " + base_image[3])
