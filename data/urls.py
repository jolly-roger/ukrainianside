import sqlite3


def getUrlByAlias(alias):
    conn = sqlite3.connect("./data/data.db")
    cur = conn.cursor()
        
    cur.execute("select u.value from aliases as a, urls as u, relation as r "\
        "where a.id = r.alias_id and u.id = r.url_id and a.value = ?;", (alias, ))
    rawUrl = cur.fetchone()
        
    cur.close()
    conn.close()
    
    return rawUrl[0]