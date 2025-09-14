# Contains common utilities
# read data from the excel file
# read data from the csv,json file
# set the headers - application/json , application/xml

class Utils(object):
    def common_headers_json(self):
        headers = {
            "Content-Type": "application/json"
        }
        return headers

