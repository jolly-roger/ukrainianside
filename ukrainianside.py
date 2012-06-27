import cherrypy
import os.path
from cherrypy import _cperror

from content import layout


class ukrainianside(object):
    @cherrypy.expose
    def sitemap_xml(self):
        cherrypy.response.headers['Content-Type'] = "application/xml"

        return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" \
            "<!-- sitemap-generator-url=\"http://www.arnebrachhold.de\" sitemap-generator-version=\"3.2.6.2\" -->" \
            "<!-- generated-on=\"January 11, 2012 10:43 am\" -->" \
            "<urlset xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd\" xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">" \
                "<url>" \
                    "<loc>http://ukrainianside.com/</loc>" \
                    "<lastmod>2012-01-07T13:52:29+00:00</lastmod>" \
                    "<changefreq>daily</changefreq>" \
                    "<priority>1.0</priority>" \
                "</url>" \
                "<url>" \
                    "<loc>http://ukrainianside.com/2011/towns/one-day-in-odessa/</loc>" \
                    "<lastmod>2012-01-07T13:52:29+00:00</lastmod>" \
                    "<changefreq>daily</changefreq>" \
                    "<priority>1.0</priority>" \
                "</url>" \
                "<url>" \
                    "<loc>http://ukrainianside.com/2011/old-ruins/greek/trip-to-olbia/</loc>" \
                    "<lastmod>2012-01-07T13:42:00+00:00</lastmod>" \
                    "<changefreq>daily</changefreq>" \
                    "<priority>1.0</priority>" \
                "</url>" \
                "<url>" \
                    "<loc>http://ukrainianside.com/2012/information/national-archaeological-park-olbia/</loc>" \
                    "<lastmod>2012-01-07T13:33:01+00:00</lastmod>" \
                    "<changefreq>daily</changefreq>" \
                    "<priority>1.0</priority>" \
                "</url>" \
                "<url>" \
                    "<loc>http://ukrainianside.com/2011/information/odessa-region-trains-timetable/</loc>" \
                    "<lastmod>2011-12-16T12:26:55+00:00</lastmod>" \
                    "<changefreq>daily</changefreq>" \
                    "<priority>1.0</priority>" \
                "</url>" \
                "<url>" \
                    "<loc>http://ukrainianside.com/2011/general/introduction/</loc>" \
                    "<lastmod>2011-12-16T12:22:29+00:00</lastmod>" \
                    "<changefreq>daily</changefreq>" \
                    "<priority>1.0</priority>" \
                "</url>" \
                "<url>" \
                    "<loc>http://ukrainianside.com/category/towns/</loc>" \
                    "<changefreq>weekly</changefreq>" \
                    "<priority>0.3</priority>" \
                "</url>" \
                "<url>" \
                    "<loc>http://ukrainianside.com/category/old-ruins/greek/</loc>" \
                    "<changefreq>weekly</changefreq>" \
                    "<priority>0.3</priority>" \
                "</url>" \
                "<url>" \
                    "<loc>http://ukrainianside.com/category/information/</loc>" \
                    "<changefreq>weekly</changefreq>" \
                    "<priority>0.3</priority>" \
                "</url>" \
                "<url>" \
                    "<loc>http://ukrainianside.com/category/general/</loc>" \
                    "<changefreq>weekly</changefreq>" \
                    "<priority>0.3</priority>" \
                "</url>" \
            "</urlset>"
    
    @cherrypy.expose
    def index(self):
        return layout.getIndex()
    
    @cherrypy.expose
    def default(self, year = None, category = None, subcategory = None, title = None):
        if year is None and category is None and subcategory is None and title is None:
            return layout.getHome()
        elif year == '2011' and category == 'towns' and subcategory == 'one-day-in-odessa' and title is None:
            return layout.getOneDayInOdessa()
        elif year == '2011' and category == 'old-ruins' and subcategory == 'greek' and title == 'trip-to-olbia':
            return layout.getTripToOlbia()
        elif year == '2011' and category == 'information' and subcategory == 'odessa-region-trains-timetable' and title is None:
            return layout.getOdessaRegionTrainsTimetable()
        elif year == '2011' and category == 'general' and subcategory == 'introduction' and title is None:
            return layout.getIntroduction()
        elif year == '2012' and category == 'information' and subcategory == 'national-archaeological-park-olbia' and title is None:
            return layout.getNationalArchaeologicalParkOlbia()
        elif year == 'category' and category == 'towns' and subcategory is None and title is None:
            return layout.getTowns()
        elif year == 'category' and category == 'information' and subcategory is None and title is None:
            return layout.getInformation()
        elif year == 'category' and category == 'general' and subcategory is None and title is None:
            return layout.getGeneral()
        elif year == 'category' and category == 'old-ruins' and subcategory == 'greek' and title is None:
            return layout.getGreek()
        else:
            return layout.getHome()


#def error_page_default(status, message, traceback, version):
#    return "Error"
#
#cherrypy.config.update({'error_page.default': error_page_default})



ukrainiansideconf = os.path.join(os.path.dirname(__file__), "ukrainianside.conf")

cherrypy.quickstart(ukrainianside(), config=ukrainiansideconf)