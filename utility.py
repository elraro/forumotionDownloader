from robobrowser import RoboBrowser

def login(user, password):
    browser = RoboBrowser(parser="lxml", user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0 (Pale Moon)")
    browser.open('http://jk-ng.foroactivo.com/login')
    login = browser.get_form(action='/login')
    login['username'].value = user
    login['password'].value = password
    browser.submit_form(login)
    return browser
