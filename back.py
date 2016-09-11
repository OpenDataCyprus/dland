import tornado.escape
import tornado.web
import tornado.ioloop
import tornado.httpserver
import json
import random
import os
import random
import operator
#import pdb

class region_handler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")

    def options(self, *args):
        self.set_header("Access-Control-Allow-Headers", "x-requested-with, content-type, accept, origin, authorization, credentials")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self, *args):
        if args[0] == "cyprus":
            with open('cyprus.geojson','r') as f:
                resp = f.read()
        elif args[0] == "nicosia":
            with open('nicosia.geojson','r') as f:
                resp = f.read()
        elif args[0] == "limassol":
            with open('limassol.geojson','r') as f:
                resp = f.read()
        elif args[0] == "larnaca":
            with open('larnaca.geojson','r') as f:
                resp = f.read()
        elif args[0] == "paphos":
            with open('paphos.geojson','r') as f:
                resp = f.read()
        elif args[0] == "famagusta":
            with open('famagusta.geojson','r') as f:
                resp = f.read()
        #elif args[0] == "kerynia":
        self.write(resp)

class centroid_handler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")

    def options(self):
        self.set_header("Access-Control-Allow-Headers", "x-requested-with, content-type, accept, origin, authorization, credentials")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        with open('centroids.geojson','r') as f:
            cen_data = f.read()
        cen_data = json.loads(cen_data)
        cen_dict = dict()
        for cen in cen_data["features"]:
            cen_dict[cen["properties"]["POST_CODE"]] = cen["geometry"]["coordinates"]
        resp = json.dumps(cen_dict)
        self.write(resp)

class data_handler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")

    def options(self, *args):
        self.set_header("Access-Control-Allow-Headers", "x-requested-with, content-type, accept, origin, authorization, credentials")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self, *args):
        if args[0] == "pharmacies":
            with open('pharmacy_count.txt','r') as f:
                resp = f.read()
        #elif args[0] == "":
        self.write(resp)

class optimize_placement_handler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")

    def options(self):
        self.set_header("Access-Control-Allow-Headers", "x-requested-with, content-type, accept, origin, authorization, credentials")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        criteria = self.get_argument("criteria")
        competition = self.get_argument("competition")
        region = self.get_argument("region")

        if region == "cyprus":
            with open('cyprus.geojson','r') as f:
                region_data = f.read()
        elif region == "nicosia":
            with open('nicosia.geojson','r') as f:
                region_data = f.read()
        elif region == "limassol":
            with open('limassol.geojson','r') as f:
                region_data = f.read()
        elif region == "larnaca":
            with open('larnaca.geojson','r') as f:
                region_data = f.read()
        elif region == "paphos":
            with open('paphos.geojson','r') as f:
                region_data = f.read()
        elif region == "famagusta":
            with open('famagusta.geojson','r') as f:
                region_data = f.read()
        #elif args[0] == "kerynia":  # :(
        region_data = json.loads(region_data)
        if competition == "pharmacy":
            with open('pharmacy_count.txt','r') as f:
                comp_data = f.read()
        #elif competition == "":
        comp_data = json.loads(comp_data)
        criteria = json.loads(criteria)

        # Loop through criteria to fetch the corresponding values
        postcode_score = dict()
        for fe in region_data["features"]:
            temp_score = 0
            for cr in criteria:
                temp_score = temp_score + int(fe["properties"][cr])
            postcode_score[fe["properties"]["POST_CODE"]] = temp_score

        # Scoring Algorithm
        max_score = postcode_score[max(postcode_score, key=postcode_score.get)]
        #max_score = max(postcode_score.iteritems(), key=operator.itemgetter(1))[0]
        for fe in region_data["features"]:
            this_postcode = fe["properties"]["POST_CODE"]
            fe["properties"]["colorMap"] = str(int(round(float(postcode_score[this_postcode])/max_score*20)))
            if str(this_postcode) in comp_data:
                fe["properties"]["comp_count"] = comp_data[str(this_postcode)]
            else:
                fe["properties"]["comp_count"] = 0
        self.write(json.dumps(region_data))


settings = {
    "cookie_secret": "dummy",
    "compress_response":"True",
    "debug":"True"
}

application = tornado.web.Application([
        (r"/region/(.*)?", region_handler),
        (r"/centroids", centroid_handler),
        (r"/data/(.*)?", data_handler),
        (r"/optimize_placement", optimize_placement_handler)
], **settings)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
