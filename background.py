#!/usr/bin/env python

import sys, urllib2, logging
from base import Base

class BackgroundTiles(Base):
    maxZoom = 18
    url = ""
    subdomains = None
    url1 = "" # url1 and url2 are url parts if subdomains are provided
    url2 = ""

    def getTileUrl(self, zoom, x, y, tileCounter):
        #return "http://www.yota.ru/images/y.coverage/tiles/%s/%s-%s.png" % (zoom, x, y)
        #return "http://www.yota.ru/images/y.coverage.2014-08/tiles/%s/%s-%s.png" % (zoom, x, y)
        return "http://c.tiles.mapbox.com/v3/timrobertson100.map-c9rscfra/%s/%s/%s.png" % (zoom, x, y)
       

    def getMaxZoom(self, bbox):
        return self.maxZoom

    def getTileImage(self, zoom, x, y, counter):
        url = self.getTileUrl(zoom, x, y, counter)
        try:
            tile = urllib2.urlopen(url).read()
        except Exception, e:
            # Something went wrong
            logging.error(e)
            logging.error("Unable to download image %s" % url)
            sys.exit(-1)
        return tile		