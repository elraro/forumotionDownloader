from robobrowser import RoboBrowser
from forum import Forum

def login(user, password, forum):
    browser = RoboBrowser(parser="lxml", user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0 (Pale Moon)")
    browser.open(forum + "/login")
    login = browser.get_form(action="/login")
    login["username"].value = user
    login["password"].value = password
    browser.submit_form(login)
    return browser

def findForums(browser, forumList):
    for forum in browser.parsed.findAll("dd", "dterm"):
        forums = forum.findAll("a", "forumtitle")
        if forums is not None:
            for a in forums:
                link = a["href"]
                id = link.split("-")[0][2:]
                name = a.contents[0]
                print("Create forum " + name + " with id " + str(id))
                forumList.append(Forum(id, str(name), link))

        subforums = forum.findAll("a", "gensmall")
        if subforums is not None:
            for subforum in subforums:
                link = subforum["href"]
                id = link.split("-")[0][2:]
                name = subforum.contents[0]
                print("Create forum " + name + " with id " + str(id))
                forumList.append(Forum(id, str(name), link))