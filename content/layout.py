import cherrypy
import random

from jinja2 import Environment, FileSystemLoader

import data


env = None


def getenv():
    global env
    
    if env is None:
        env = Environment(loader = FileSystemLoader(cherrypy.request.app.config["ukrainianside"]["base_dir"] + \
            "content"))
        env.globals["postedIn"] = "Опубликована в "
        env.globals["continueReading"] = "Читать далее "
        
        env.globals["getUrlByAlias"] = data.urls.getUrlByAlias
        
        env.globals["getNameByAlias"] = data.names.getNameByAlias
        
        env.globals["randint"] = random.randint
        
        env.globals["getAticleDescByAlias"] = data.descs.getAticleDescByAlias
        
        env.globals["getCategoryAliasByAticleAlias"] = data.categories.getCategoryAliasByAticleAlias
        
        env.globals["getAticlesSeq"] = data.seq.getAticlesSeq
        
    return env

def getCategory(categoryName):
    tmpl = getenv().get_template("pages/" + categoryName + ".html")
    return tmpl.render()

def getAticle(aticleName):
    tmpl = getenv().get_template("pages/" + aticleName + ".html")
    return tmpl.render()

def getIndex():
    return getHome()
    
def getHome():
    tmpl = getenv().get_template("pages/home.html")
    return tmpl.render()