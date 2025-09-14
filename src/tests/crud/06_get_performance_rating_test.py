import json
import pytest
import logging
import requests  # This is use to print the messages - Logs
from src.helpers.api_requests_wrapper import get_request
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import *  # import all the verification
from src.utils.utils import Utils

class TestGetPerformanceRating:
    @pytest.mark.Get_Performance_Rating_test
    def test_get_performance_rating(self):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("Starting the Testcase of TestGetPerformanceRating Test")
        # now returns both
        response, response_json = get_request(
            url=APIConstants().Get_Performance_Rating_url(),
            auth=None,
            headers=None,
            in_json=True
        )
        LOGGER.info("GET Get_Performance_Rating.")
        LOGGER.info("Now Verify")

        # Verify status code    
        verify_http_status_code(response, 200)
        LOGGER.info("Verified the Status Code 200")

        # Verify content-type header
        verify_response_header(response, "Content-Type", "application/json")
        LOGGER.info("Verified the Content-Type header")
         
        # Pretty-print JSON body
        print(json.dumps(response_json, indent=4))
        LOGGER.info(json.dumps(response_json, indent=4))
        LOGGER.info("Testcase of TestGetEmployeeDetails is Done")



