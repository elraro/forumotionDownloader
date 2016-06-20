from robobrowser import RoboBrowser
from forum import Forum
import config

def login(user, password, forum):
    browser = RoboBrowser(parser="lxml", user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0 (Pale Moon)")
    browser.open(forum + "/login")
    login = browser.get_form(action="/login")
    login["username"].value = user
    login["password"].value = password
    browser.submit_form(login)
    return browser

def findForums(browser, forumList, url):
    browser.open(url)
    forumListAux = {}
    for forum in browser.parsed.findAll("dd", "dterm"):
        forums = forum.findAll("a", "forumtitle")
        if forums is not None:
            for a in forums:
                link = a["href"]
                if "http://" in link:
                    continue

                id = link.split("-")[0][2:]
                if id in forumList:
                    continue

                try:
                    name = a.contents[0]
                except IndexError:
                    continue

                print("Create forum " + name + " with id " + str(id))
                forumListAux[id] = Forum(id, str(name), link)

        subforums = forum.findAll("a", "gensmall")
        if subforums is not None:
            for subforum in subforums:
                link = subforum["href"]
                if "http://" in link:
                    continue

                id = link.split("-")[0][2:]
                if id in forumList:
                    continue

                try:
                    name = subforum.contents[0]
                except IndexError:
                    continue

                print("Create forum " + name + " with id " + str(id))
                forumListAux[id] = Forum(id, str(name), link)

    if len(forumListAux) != 0:
        forumList.update(forumListAux)
        for forum in forumListAux:
            print("Lets check subforums in " + config.getForum() + forumListAux[forum].link)
            findForums(browser, forumList, config.getForum() + forumListAux[forum].link)

def downloadUsers(browser, userList, url):
    browser.open(url)
    admin = browser.parsed.find("p", "copyright").find("a")
    print(admin["href"])
    browser.open(url + admin["href"])

    for option in browser.parsed.findAll("a"):
        try:
            if "part=users_groups&tid=" in option["href"]:
                browser.open(url + option["href"])
                print(option["href"])
                break
        except KeyError:
            continue

    for option in browser.parsed.findAll("a"):
        try:
            if "part=users_groups&sub=users&tid=" in option["href"]:
                browser.open(url + option["href"])
                print(option["href"])
                break
        except KeyError:
            continue

    print(browser.parsed)