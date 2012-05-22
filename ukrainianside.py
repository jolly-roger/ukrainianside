import cherrypy
import os.path
from cherrypy import _cperror


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
    def default(self, year = None, category = None, subcategory = None, title = None):
        if year is None and category is None and subcategory is None and title is None:
            home = open(cherrypy.request.app.config["ukrainianside"]["base_dir"]+ "home.html", encoding="utf-8").read()
        
            return home
        elif year is not None and category is not None and subcategory is not None and title is not None:
            filename = cherrypy.request.app.config["ukrainianside"]["base_dir"] + str(year) + "/" + category + "/" + subcategory
            
            if title is not None:
                filename += "/" + title + ".html"
            else:
                filename += ".html"
            
            article = open(filename, encoding="utf-8").read()
        
            return article
        elif year is not None and category is not None and subcategory is not None:
            filename = cherrypy.request.app.config["ukrainianside"]["base_dir"] + str(year) + "/" + category + "/" + subcategory + ".html"
            
            article = open(filename, encoding="utf-8").read()
        
            return article
        elif year is not None and category is not None:
            filename = cherrypy.request.app.config["ukrainianside"]["base_dir"] + str(year) + "/" + category + ".html"
            
            article = open(filename, encoding="utf-8").read()
        
            return article


def error_page_default(status, message, traceback, version):
    return "Error"

cherrypy.config.update({'error_page.default': error_page_default})



ukrainiansideconf = os.path.join(os.path.dirname(__file__), "ukrainianside.conf")

cherrypy.quickstart(ukrainianside(), config=ukrainiansideconf)