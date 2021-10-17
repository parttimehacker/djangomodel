#!/usr/bin/python3
""" DIYHA Application Configuration Initializer """

# The MIT License (MIT)
#
# Copyright (c) 2019 parttimehacker@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import argparse
import logging
import logging.config
import requests
import json
import socket

class DjangoModel:
    """ Command line arguement model which expects an MQTT broker hostname or IP address,
        the location topic for the device and an option mode for the switch.
    """

    def __init__(self,logging_file):
        """ Parse the command line arguements """
        logging.config.fileConfig( fname=logging_file, disable_existing_loggers=False )
        # Get the logger specified in the file
        self.logger = logging.getLogger(__name__)
        self.headers = {'Content-type': 'application/json'}

    def set_urls(self, webserver):
        """ MQTT BORKER hostname or IP address."""
        self.server = socket.gethostname()
        print("set_urls: " + self.server)
        self.server_status_url = webserver + "/server/status"
        self.server_status_detail_url = webserver + "/server/status/detail"
        self.server_asset_url = webserver + "/server/asset"
        self.server_asset_detail_url = webserver + "/server/asset/detail"
        self.environment_url = webserver + "/environment"
        self.environment_detail_url = webserver + "/environment/detail"
        self.motion_url = webserver + "/motion"
        self.motion_detail_url = webserver + "/motion/detail"
                                
    def get_server_id(self,):
        url = self.server_status_url
        try:
            response = requests.get(url)
            servers = response.json()
            for server in servers:
                print("get_server_id: "+server["name"])
                if self.server == server["name"]:
                    self.sid = server["id"]
                    break
            # response.raise_for_status()
            # Code here will only run if the request is successful
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)
            
            
    def get_environment_id(self,):
        url = self.environment_url
        try:
            response = requests.get(url)
            locations = response.json()
            for location in locations:
                # print("get_server_id: "+server["name"])
                if self.location == location["name"]:
                    self.eid = location["id"]
                    break
            # response.raise_for_status()
            # Code here will only run if the request is successful
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)

    def get_motion_id(self,):
        url = self.motion_url
        try:
            response = requests.get(url)
            location = response.json()
            for location in locations:
                # print("get_server_id: "+server["name"])
                if self.location == location["name"]:
                    self.mid = location["id"]
                    break
            # response.raise_for_status()
            # Code here will only run if the request is successful
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)
            

    def put_server_status(self, info):
        """ put json cpu status to the django server """  
        info["id"] = self.id  
        url = self.server_status_detail_url + "/" + str(self.id)
        try:
            response = requests.put(url, data=json.dumps(info), headers=self.headers)
            response.raise_for_status()
            # Code here will only run if the request is successful
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)
        
    def put_server_asset(self, info):
        """ put json cpu status to the django server """  
        info["id"] = self.id  
        url = self.server_asset_detail_url + "/" + str(self.id)
        try:
            response = requests.put(url, data=json.dumps(info), headers=self.headers)
            response.raise_for_status()
            # Code here will only run if the request is successful
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)


