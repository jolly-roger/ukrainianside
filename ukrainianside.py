import cherrypy
import os.path
import smtplib
from cherrypy import _cperror
from email.mime.text import MIMEText

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
        if year == 'category':
            if title is not None:
                return layout.getCategory(title)
            elif subcategory is not None:
                return layout.getCategory(subcategory)
            elif category is not None:
                return layout.getCategory(category)
        else:
            if title is not None:
                return layout.getAticle(title)
            elif subcategory is not None:
                return layout.getAticle(subcategory)
        
        return layout.getHome()


def error_page_default(status, message, traceback, version):
    sender = 'www@dig-dns.com (www)'
    recipient = 'roger@dig-dns.com'
    
    text = 'Status: ' + status + '\n\n' + 'Message: ' + message + '\n\n' +\
        'Traceback: ' + traceback + '\n\n' + 'Version: ' + version
    
    msg = MIMEText(text)
    msg['Subject'] = 'Ukrainianside error'
    msg['From'] = sender
    msg['To'] = recipient

    s = smtplib.SMTP('localhost')
    s.sendmail(sender, recipient, msg.as_string())
    s.quit()
    
    return "Error"

cherrypy.config.update({'error_page.default': error_page_default})



ukrainiansideconf = os.path.join(os.path.dirname(__file__), "ukrainianside.conf")

cherrypy.quickstart(ukrainianside(), config=ukrainiansideconf)