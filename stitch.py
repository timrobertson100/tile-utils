#!/usr/bin/env python

# Example parameters
# python stitch.py 26.7188,58.3786,26.72067,58.3791 bing
# python stitch.py 26.7188,58.3786,26.72067,58.3791 http://{a,b,c}.tile.openstreetmap.org
# python stitch.py -- -77.0471,38.8790,-77.0299,38.8891 ..\tiles.mbtiles

import sys, os, argparse, logging

from bing_aerial import BingAerial
from osm_tiles import OsmTiles
from mbtiles import Mbtiles
from gbif import GBIFTiles
from background import BackgroundTiles

parser = argparse.ArgumentParser()
parser.add_argument("bbox", help="area bbox coordinates in the form left,bottom,right,top; example: 26.7188,58.3786,26.72067,58.3791")
parser.add_argument("source", help="source for tiles; example values: bing, http://{a,b,c}.tile.openstreetmap.org, pathTo/fileName.mbtiles")
parser.add_argument("-z", "--zoom", type=int, help="desired zoom")
parser.add_argument("-o", "--output", help="result image name, extension (.png or .jpg) defines image format type")
args = parser.parse_args()

# preparing bbox
bbox = [float(i) for i in args.bbox.split(",")]

if args.source == "bing":
	tiles = BingAerial()
elif args.source == "gbif":
	tiles = GBIFTiles()
elif args.source == "base":
	tiles = BackgroundTiles()
elif len(args.source)>7 and args.source[:7] == "http://":
	tiles = OsmTiles(args.source)
elif len(args.source)>8 and os.path.isfile(args.source) and args.source[-8:] == ".mbtiles":
	tiles = Mbtiles(args.source)
else:
	logging.error("Unknown tile source")
	sys.exit(-1)

tiles.stitch(bbox, args.zoom, output=args.output)
