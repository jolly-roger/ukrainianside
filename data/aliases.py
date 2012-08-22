import sqlite3


def getAll():
    conn = sqlite3.connect(cherrypy.request.app.config["ukrainianside"]["base_dir"] + "data/data.db")
    cur = conn.cursor()
        
    cur.execute("select value from aliases;")
    rawAliases = cur.fetchall()
        
    cur.close()
    conn.close()
    
    return rawAliases