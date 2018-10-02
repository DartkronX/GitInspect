# GitInspect

An OSINT tool to search thru all specific user's github repositories for specific string.
As we know sometimes when you compile a program , your computers specific info such as program directories can still be seen inside(sometimes a user forgets to remove some import comments or information from the tool).

This tool gets a list of all users repositories from github api , downloads them and helps you search for specific strings in all repositories and all commits .

# Usage :

! the terminal should be open in the same directory(where we download all the projects/repositories) the tool is and runned from there !

 gitinspect.py -d -u Dartkronx //// Downloads all user's repositories to current directory !!! This is the first step before searching for a string

 gitinspect.py -u Dartkronx -s "StringToSearchFor" /// Get list of repositories from the web(api.github.com/users/user/repos) , and search for string(not case sensitive)

 gitinspect.py -s "StringToSearchFor" /// Search for a string in the git Directories you already downloaded (current location)(doesnt check users gethub api for proper list)

! the terminal should be open in the same directory(where we download all the projects/repositories) the tool is and runned from there !

Can add a better graph for the info gathered later.

Enjoy
