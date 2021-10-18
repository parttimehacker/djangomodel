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

import logging
import logging.config
import socket
import json
import requests

HEADERS = {'Content-type': 'application/json'}

class DjangoModel:
    """ Command line arguement model which expects an MQTT broker hostname or IP address,
        the location topic for the device and an option mode for the switch.
    """

    def __init__(self, logging_file):
        """ Parse the command line arguements """
        logging.config.fileConfig(fname=logging_file, disable_existing_loggers=False)
        # Get the logger specified in the file
        self.logger = logging.getLogger(__name__)
        self.urls = {"status": "/server/status", "assets": "/server/asset", \
            "environment": "/environment", "motion": "/motion"}
        self.ids = {"server": 0, "environment": 0, "motion": 0}

    def set_django_urls(self, webserver):
        """ MQTT BORKER hostname or IP address."""
        self.urls["status"] = webserver + self.urls["status"]
        self.urls["assets"] = webserver + self.urls["assets"]
        self.urls["environment"] = webserver + self.urls["environment"]
        self.urls["motion"] = webserver + self.urls["motion"]

    def get_server_id(self,):
        """ MQTT BORKER hostname or IP address."""
        try:
            response = requests.get(self.urls["status"])
            servers = response.json()
            host = socket.gethostname()
            for server in servers:
                if host == server["name"]:
                    self.ids["server"] = server["id"]
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
        """ MQTT BORKER hostname or IP address."""
        try:
            response = requests.get(self.urls["environment"])
            locations = response.json()
            host = socket.gethostname()
            for location in locations:
                # print("get_server_id: "+server["name"])
                if host == location["name"]:
                    self.ids["environment"] = location["id"]
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
        """ MQTT BORKER hostname or IP address."""
        try:
            response = requests.get(self.urls["motion"])
            locations = response.json()
            host = socket.gethostname()
            for location in locations:
                if host == location["name"]:
                    self.ids["motion"] = location["id"]
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
        info["id"] = self.ids["server"]
        url = self.urls["status"] + "/" + str(self.ids["server"])
        try:
            response = requests.put(url, data=json.dumps(info), headers=HEADERS)
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
        info["id"] = self.ids["server"]
        url = self.urls["asset"]  + "/" + str(self.ids["server"])
        try:
            response = requests.put(url, data=json.dumps(info), headers=HEADERS)
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
