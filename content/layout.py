import cherrypy

from jinja2 import Environment, FileSystemLoader


env = None


def getenv():
    global env
    
    if env is None:
        env = Environment(loader = FileSystemLoader(cherrypy.request.app.config["ukrainianside"]["base_dir"] + \
            "content\pages"))
        
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

def getOdessaRegionTrainsTimetable():
    tmpl = getenv().get_template("odessa-region-trains-timetable.html")
    return tmpl.render()

def getIntroduction():
    tmpl = getenv().get_template("introduction.html")
    return tmpl.render()

def getNationalArchaeologicalParkOlbia():
    tmpl = getenv().get_template("national-archaeological-park-olbia.html")
    return tmpl.render()

def getTowns():
    tmpl = getenv().get_template("towns.html")
    return tmpl.render()

def getInformation():
    tmpl = getenv().get_template("information.html")
    return tmpl.render()

def getGeneral():
    tmpl = getenv().get_template("general.html")
    return tmpl.render()

def getGreek():
    tmpl = getenv().get_template("greek.html")
    return tmpl.render()