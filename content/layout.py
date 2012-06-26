import cherrypy

from jinja2 import Environment, FileSystemLoader


env = None


def getenv():
    global env
    
    if env is None:
        env = Environment(loader = FileSystemLoader(cherrypy.request.app.config["ukrainianside"]["base_dir"] + \
            "content"))
        
    return env

def getIndex():
    return getHome()
    
def getHome():
    tmpl = getenv().get_template("home.html")
    return tmpl.render()

def getOneDayInOdessa():
    tmpl = getenv().get_template("one-day-in-odessa.html")
    return tmpl.render()

def getTripToOlbia():
    tmpl = getenv().get_template("trip-to-olbia.html")
    return tmpl.render()