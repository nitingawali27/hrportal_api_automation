class APIConstants:
    # Define default employee code here
    EMPLOYEE_CODE = "AASPL-1918"

    # Base URL
    def base_url(self):
        return "http://training.alignedautomation.com:8009"

    # API to search employees
    def Get_Search_Employee_Data_url(self):
        return self.base_url() + "/search_employee/"

    # API to get employee details
    def Get_Employee_Details_url(self, employee_code=None):
        # Use default EMPLOYEE_CODE if none provided
        if employee_code is None:
            employee_code = self.EMPLOYEE_CODE
        return self.base_url() + "/employee_details/" + str(employee_code)

    # API to get work and education experience
    def Get_Work_and_Education_Experience_url(self, employee_code=None):
        # Use default EMPLOYEE_CODE if none provided
        if employee_code is None:
            employee_code = self.EMPLOYEE_CODE
        return self.base_url() + "/get_work_and_education_experience/" + str(employee_code)

    # API to get reporting manager details
    def Get_Reporting_Manager_Details_url(self, employee_code=None):
        # Use default EMPLOYEE_CODE if none provided
        if employee_code is None:
            employee_code = self.EMPLOYEE_CODE
        return self.base_url() + "/get_reporting_manager_details/" + str(employee_code)

    # API to get employee skill data
    def Get_Employee_Skill_Data_url(self, employee_code=None):
        # Use default EMPLOYEE_CODE if none provided
        if employee_code is None:
            employee_code = self.EMPLOYEE_CODE
        return self.base_url() + "/get_employee_skill_data/" + str(employee_code)
    
      # API to get performance rating
    def Get_Performance_Rating_url(self, employee_code=None):
        # Use default EMPLOYEE_CODE if none provided
        if employee_code is None:
            employee_code = self.EMPLOYEE_CODE
        return self.base_url() + "/get_performance_rating/" + str(employee_code)
    
    # API to get project details
    def Get_Project_Details_url(self, employee_code=None):
        # Use default EMPLOYEE_CODE if none provided
        if employee_code is None:
            employee_code = self.EMPLOYEE_CODE
        return self.base_url() + "/project_details/" + str(employee_code)

    # API to get all projects
    def Get_All_Projects_url(self, employee_code=None):
        # Use default EMPLOYEE_CODE if none provided
        if employee_code is None:
            employee_code = self.EMPLOYEE_CODE
        return self.base_url() + "/projects/" + str(employee_code)
    
    # API to get employee attendance details
    def Get_Employee_Attendance_url(self, employee_code=None):
        # Use default EMPLOYEE_CODE if none provided
        if employee_code is None:
            employee_code = self.EMPLOYEE_CODE
        return self.base_url() + "/attendance/" + str(employee_code)

    # API to get employee certificates details
    def Get_Employee_Certificates_url(self, employee_code=None):
        # Use default EMPLOYEE_CODE if none provided
        if employee_code is None:
            employee_code = self.EMPLOYEE_CODE
        return self.base_url() + "/certificates/" + str(employee_code)
    
            # API to get associates under manager
    def Get_Associates_Under_Manager_url(self, employee_code=None):
          # Use default EMPLOYEE_CODE if none provided
          if employee_code is None:
                employee_code = self.EMPLOYEE_CODE
          return self.base_url() + "/associates_under_manager/" + str(employee_code)
    
  