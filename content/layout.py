import cherrypy

from jinja2 import Environment, FileSystemLoader

from data import urls


env = None


def getenv():
    global env
    
    if env is None:
        env = Environment(loader = FileSystemLoader(cherrypy.request.app.config["ukrainianside"]["base_dir"] + \
            "content"))
        env.globals["postedIn"] = "Опубликована в "
        env.globals["continueReading"] = "Читать далее "
        
        env.globals["getCategoryUrlByAlias"] = urls.getCategoryUrlByAlias
        
    return env

def getIndex():
    return getHome()
    
def getHome():
    tmpl = getenv().get_template("pages/home.html")
    return tmpl.render()

def getOneDayInOdessa():
    tmpl = getenv().get_template("pages/one-day-in-odessa.html")
    return tmpl.render()

def getTripToOlbia():
    tmpl = getenv().get_template("pages/trip-to-olbia.html")
    return tmpl.render()

def getOdessaRegionTrainsTimetable():
    tmpl = getenv().get_template("pages/odessa-region-trains-timetable.html")
    return tmpl.render()

def getIntroduction():
    tmpl = getenv().get_template("pages/introduction.html")
    return tmpl.render()

def getNationalArchaeologicalParkOlbia():
    tmpl = getenv().get_template("pages/national-archaeological-park-olbia.html")
    return tmpl.render()

def getTripToKinburnPeninsula():
    tmpl = getenv().get_template("pages/trip-to-kinburn-peninsula.html")
    return tmpl.render()

def getTowns():
    tmpl = getenv().get_template("pages/towns.html")
    return tmpl.render()

def getInformation():
    tmpl = getenv().get_template("pages/information.html")
    return tmpl.render()

def getGeneral():
    tmpl = getenv().get_template("pages/general.html")
    return tmpl.render()

def getGreek():
    tmpl = getenv().get_template("pages/greek.html")
    return tmpl.render()

def getNature():
    tmpl = getenv().get_template("pages/nature.html")
    return tmpl.render()