import sqlite3
import cherrypy


def getAll():
    #conn = sqlite3.connect(cherrypy.request.app.config["ukrainianside"]["base_dir"] + "data/data.db")
    conn = sqlite3.connect('/home/www/ukrainianside/' + "data/data.db")
    cur = conn.cursor()
        
    cur.execute("select value from aliases;")
    rawAliases = cur.fetchall()
        
    cur.close()
    conn.close()
    
    return rawAliases