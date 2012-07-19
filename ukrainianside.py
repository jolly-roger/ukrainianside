import cherrypy
import os.path
from cherrypy import _cperror

from content import layout

import sitemap


class ukrainianside(object):
    @cherrypy.expose
    def sitemap_xml(self):
        cherrypy.response.headers['Content-Type'] = "application/xml"

        return sitemap.getSitemap() 
    
    @cherrypy.expose
    def index(self):
        return layout.getIndex()
    
    @cherrypy.expose
    def default(self, year = None, category = None, subcategory = None, title = None, *args, **kwargs):
        if year is None and category is None and subcategory is None and title is None:
            return layout.getHome()
        elif year == '2011' and category == 'towns' and subcategory == 'one-day-in-odessa' and title is None:
            return layout.getOneDayInOdessa()
        elif year == '2011' and category == 'old-ruins' and subcategory == 'greek' and title == 'trip-to-olbia':
            return layout.getTripToOlbia()
        elif year == '2012' and category == 'old-ruins' and subcategory == 'greek' and title == 'visit-bilhorod-dnistrovskyi':
            return layout.getVisitBilhorodDnistrovskyi()
        elif year == '2011' and category == 'information' and subcategory == 'odessa-region-trains-timetable' and title is None:
            return layout.getOdessaRegionTrainsTimetable()
        elif year == '2011' and category == 'general' and subcategory == 'introduction' and title is None:
            return layout.getIntroduction()
        elif year == '2012' and category == 'information' and subcategory == 'national-archaeological-park-olbia' and title is None:
            return layout.getNationalArchaeologicalParkOlbia()
        elif year == '2012' and category == 'nature' and subcategory == 'trip-to-kinburn-peninsula' and title is None:
            return layout.getTripToKinburnPeninsula()
        elif year == 'category' and category == 'towns' and subcategory is None and title is None:
            return layout.getTowns()
        elif year == 'category' and category == 'information' and subcategory is None and title is None:
            return layout.getInformation()
        elif year == 'category' and category == 'general' and subcategory is None and title is None:
            return layout.getGeneral()
        elif year == 'category' and category == 'old-ruins' and subcategory == 'greek' and title is None:
            return layout.getGreek()
        elif year == 'category' and category == 'nature' and subcategory is None and title is None:
            return layout.getNature()
        else:
            return layout.getHome()


def error_page_default(status, message, traceback, version):
    return "Error"

cherrypy.config.update({'error_page.default': error_page_default})



ukrainiansideconf = os.path.join(os.path.dirname(__file__), "ukrainianside.conf")

cherrypy.quickstart(ukrainianside(), config=ukrainiansideconf)