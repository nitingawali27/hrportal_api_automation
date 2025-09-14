import json
import pytest
import logging
import requests  # This is use to print the messages - Logs
from src.helpers.api_requests_wrapper import get_request
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import *  # import all the verification
from src.utils.utils import Utils

class TestGetWorkAndEducationExperience:
    @pytest.mark.Get_Work_and_Education_Experience_test
    def test_get_work_and_education_experience(self):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("Starting the Testcase of TestGetWorkAndEducationExperience Test")
        # now returns both
        response, response_json = get_request(
            url=APIConstants().Get_Work_and_Education_Experience_url(),
            auth=None,  
            headers=None,
            in_json=True
        )
        LOGGER.info("GET Get_Work_and_Education_Experience.")
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



