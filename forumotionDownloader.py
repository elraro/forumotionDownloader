import utility
import config

if(config.getUsername() is None or config.getPassword() is None):
    print("Please set username and password in the config.py file.")
    exit(1)

if(config.getForum() is None):
    print("Please set forum to dump in the config.py file.")
    exit(1)

browser = utility.login(config.getUsername(), config.getPassword(), config.getForum())

browser.open(config.getForum() + "/forum")
forumList = []

utility.findForums(browser, forumList)

print(forumList)