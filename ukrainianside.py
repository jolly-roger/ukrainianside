import cherrypy
import json
import os.path
import urllib.request
import urllib.parse
import traceback
import logging


from .content import layout
from .data import aliases

from . import sitemap


logger = logging.getLogger('werp_error.ukrainianside')


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
        try:
            als = aliases.getAll()
            
            isexist = False
            
            if category is not None:
                if aliases.isExist(category, als): isexist = True
                else: isexist = False
            if subcategory is not None:
                if aliases.isExist(subcategory, als): isexist = True
                else: isexist = False
            if title is not None:
                if aliases.isExist(title, als): isexist = True
                else: isexist = False
    
            if isexist:
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
            else:    
                return layout.getHome()
        except:
            logger.exception(traceback.format_exc())
            return ''


def error_page_default(status, message, traceback, version):
    d = urllib.parse.urlencode({'status': status, 'message': message, 'traceback': traceback, 'version': version,
        'data': json.dumps({'subject': 'Ukrainianside error',
            'base': cherrypy.request.base, 'request_line': cherrypy.request.request_line,
            'headers': str(cherrypy.request.headers)})})
    d = d.encode('utf-8')
    req = urllib.request.Request('http://localhost:18404/sendmail')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded;charset=utf-8')
    res = urllib.request.urlopen(req, d)
    return res.read().decode()

def wsgi():
    conf = os.path.join(os.path.dirname(__file__), "ukrainianside.conf")
    tree = cherrypy._cptree.Tree()
    app = tree.mount(ukrainianside(), config=conf)
    app.config.update({'/': {'error_page.default': error_page_default}})
    tree.bind_address = (app.config['global']['server.socket_host'], app.config['global']['server.socket_port'])
    tree.numthreads = app.config['global']['server.thread_pool']
    tree.request_queue_size = app.config['global']['server.socket_queue_size']
    return tree