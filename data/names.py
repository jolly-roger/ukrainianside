import sqlite3


def getNameByAlias(alias):
    conn = sqlite3.connect("./data/data.db")
    cur = self.conn.cursor()
        
    cur.execute("select n.value from aliases as a, names as n, alias_name as a_n "\
        "where a.id = a_n.alias_id and n.id = a_n.name_id and a.value = ?;", (alias, ))
    rawName = cur.fetchone()
        
    cur.close()
    conn.close()
    
    return rawName[0]

def getCategoryNameByAlias(alias):
    return getNameByAlias(alias)

def getAticleNameByAlias(alias):
    return getNameByAlias(alias)