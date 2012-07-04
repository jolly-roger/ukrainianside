categories = {
    'general': 'http://ukrainianside.com/category/general/',
    'greek': 'http://ukrainianside.com/category/old-ruins/greek/',
    'information': 'http://ukrainianside.com/category/information/',
    'nature': 'http://ukrainianside.com/category/nature/',
    'towns': 'http://ukrainianside.com/category/towns/'
}


def getCategoryUrlByAlias(alias):
    return categories[alias]

articles = {
    'trip-to-olbia': 'http://ukrainianside.com/2011/old-ruins/greek/trip-to-olbia/',
    'trip-to-kinburn-peninsula': 'http://ukrainianside.com/2012/nature/trip-to-kinburn-peninsula/',
    'one-day-in-odessa': 'http://ukrainianside.com/2011/towns/one-day-in-odessa/',
    'odessa-region-trains-timetable': 'http://ukrainianside.com/2011/information/odessa-region-trains-timetable/',
    'national-archaeological-park-olbia': 'http://ukrainianside.com/2012/information/national-archaeological-park-olbia/',
    'introduction': 'http://ukrainianside.com/2011/general/introduction/'
}

def getAticleUrlByAlias(alias):
    return articles[alias]