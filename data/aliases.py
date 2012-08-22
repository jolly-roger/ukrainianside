import sqlite3
import cherrypy


def getAll():
    conn = sqlite3.connect(cherrypy.request.app.config["ukrainianside"]["base_dir"] + "data/data.db")
    cur = conn.cursor()
        
    cur.execute("select value from aliases;")
    rawAliases = cur.fetchall()
        
    cur.close()
    conn.close()
    
    return rawAliases

def isExist(alias, aliases = None):
    if aliases is None:
        aliases = getAll()
    
    for al in aliases:
        if al[0] == alias:
            return True
        
    return False