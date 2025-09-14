import json
import pytest
import logging
import requests  # This is use to print the messages - Logs
from src.helpers.api_requests_wrapper import get_request
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import *  # import all the verification
from src.utils.utils import Utils

class TestGetSearchEmployeeData:
    @pytest.mark.Get_Search_Employee_Data
    def test_Get_Search_Employee_Data(self):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("Starting the Testcase of TestGetSearchEmployeeData")
        # now returns both
        response, response_json = get_request(
            url=APIConstants().Get_Search_Employee_Data_url(),
            auth=None,
            headers=None,
            in_json=True
        )
        LOGGER.info("GET Get_Search_Employee_Data.")
        LOGGER.info("Now Verify")

        # Verify status code
        verify_http_status_code(response, 200)
        LOGGER.info("Verified the Status Code 200")

        # Verify content-type header
        verify_response_header(response, "Content-Type", "application/json")
        LOGGER.info("Verified the Content-Type header")

        # Verify Response Contains Expected Key (UserSearchApi)
        verify_response_key("UserSearchApi" in response_json, True)
        LOGGER.info("Verified the Response Contains Expected Key (UserSearchApi)")

        # Verify JSON key should not be null/empty
        verify_json_key_not_null(response_json["UserSearchApi"], "UserSearchApi")
        LOGGER.info("Verified the JSON key should not be null/empty")
   
        # Pretty-print JSON body
        print(json.dumps(response_json, indent=4))
        LOGGER.info(json.dumps(response_json, indent=4))
        LOGGER.info("Testcase of TestGetSearchEmployeeData is Done")


