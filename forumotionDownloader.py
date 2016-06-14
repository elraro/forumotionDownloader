from bs4 import BeautifulSoup
import utility
import config
from forum import Forum

if(config.getUsername() is None or config.getPassword() is None):
    print("Please set username and password in the config.py file.")
    exit(1)

browser = utility.login(config.getUsername(), config.getPassword())

browser.open("http://jk-ng.foroactivo.com/forum")
forumList = []

for forum in browser.parsed.findAll('dd', 'dterm'):
    forums = forum.findAll('a','forumtitle')
    if forums is not None:
        for a in forums:
            link = a['href']
            id = link.split("-")[0][2:]
            name = a.contents[0]
            print('Voy a crear el foro ' + name + ' con id ' + str(id))
            forumList.append(Forum(id, str(name), link))

    subforums = forum.findAll('a','gensmall')
    if subforums is not None:
        for subforum in subforums:
            link = a['href']
            id = link.split("-")[0][2:]
            name = a.contents[0]
            print('Voy a crear el foro ' + name + ' con id ' + str(id))
            forumList.append(Forum(id, str(name), link))

print(forumList)