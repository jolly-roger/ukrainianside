import sqlite3
import cherrypy


def getNameByAlias(alias):
    conn = sqlite3.connect(cherrypy.request.app.config["ukrainianside"]["base_dir"] + "data/data.db")
    cur = conn.cursor()
        
    cur.execute("select n.value from aliases as a, names as n, relation as r "\
        "where a.id = r.alias_id and n.id = r.name_id and a.value = ?;", (alias, ))
    rawName = cur.fetchone()
        
    cur.close()
    conn.close()
    
    return rawName[0]