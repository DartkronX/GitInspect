#!/usr/bin/python

import time
import urllib
import urllib2
import threading
from threading import Thread, current_thread
from threading import *
from tqdm import tqdm
import requests
import os
import argparse

# documentation and info

# gitinspect.py -d -u Dartkronx //// Downloads all user's repositories to current directory !!! This is the first step before searching for a string

# gitinspect.py -u Dartkronx -s "StringToSearchFor" /// Get list of repositories from the web(api.github.com/users/user/repos) , and search for string(not case sensitive)

# gitinspect.py -s "StringToSearchFor" /// Search for a string in the git Directories you already downloaded (current location)

# the terminal should be open in the same directory the tool is and runned from there 


print "\nOpen me and read documentation\n"


parser = argparse.ArgumentParser('GitInspector')
parser.add_argument('-d' , '--download' , action='store_true',help="Download")
parser.add_argument('-u', '--username',help="username  Open me and read documentation")
parser.add_argument('-s', '--string',help="string to search for in the repository (within all commits)")
args = vars(parser.parse_args())

foo = args['download']
cheese = args['username']
srch_str = args['string']

def get_repositories(url):
 
   
    result = []
    r = requests.get(url=url)
    if 'next' in r.links :
        result += get_repositories(r.links['next']['url'])

    for repository in r.json():
        result.append(repository.get('name'))

    return result



def download(repos):
	for i in tqdm(repos):

		print "Donwloading : ",i
		os.system('git clone https://github.com/'+cheese+'/'+i+'.git')




if (args['download'] == True)  and (args['username'] != None) :

	url = "https://api.github.com/users/"+cheese+"/repos"

	print "\nGetting User repositories\n"
	
	result = get_repositories(url)

	repos = result

	print "\n\nStarting download..\n"
	
	download(repos)

elif (args['download'] == False)  and (args['username'] != None) and (args['string'] != None) :

	print "Search started..."

	url = "https://api.github.com/users/"+cheese+"/repos"

	result = get_repositories(url)

	dirlist = result

	#dirlist =  [name for name in os.listdir(".") if os.path.isdir(name)]

	for i in dirlist:
		
		print os.system("cd "+i+" && pwd &&git rev-list --all | GIT_PAGER=cat xargs git grep -i "+srch_str+" ")




elif (args['download'] == False)  and (args['username'] == None) and (args['string'] != None) :

	print "\n\nSearch started...\n\n"

	#url = "https://api.github.com/users/"+cheese+"/repos"

	#result = get_repositories(url)

	#dirlist = result

	dirlist =  [name for name in os.listdir(".") if os.path.isdir(name)]

	for i in dirlist:
		
		print os.system("cd "+i+" && pwd &&git rev-list --all | GIT_PAGER=cat xargs git grep -i "+srch_str+" ")



