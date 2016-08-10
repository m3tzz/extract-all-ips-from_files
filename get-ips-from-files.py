import re #for regular expressions - to match ip's
import sys #for parsing command line opts
import fileinput, glob, string, sys, os
from os.path import join

try:

    # create an empty list
    ips = []
    #Define path
    path = "/Users/rubenbarbosa/Desktop/Tier1_fw_new_configs/*"
    files = glob.glob(path)

    # read through the file
    for text in fileinput.input(files):
       #strip off the \n
        text = text.rstrip()
       #this is probably not the best way, but it works for now
        regex = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})$', text)
        # if the regex is not empty and is not already in ips list append
        if regex is not None and regex not in ips:
            ips.append(regex)


    #loop through the list
    for ip in ips:
        #I know there is argument as to whether the string join method is pythonic
        addy = "".join(ip)
        if addy is not '':
            print "IP: %s" % (addy)

#catch any standard error (we can add more later)
except IOError, (errno, strerror):
    print "I/O Error(%s) : %s" % (errno, strerror)
