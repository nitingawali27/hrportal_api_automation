# HR Portal API Automation - Flow & Logic

## Project Overview

This document provides a comprehensive overview of the HR Portal API Automation project, including the complete flow logic and state diagrams using Mermaid.

---

## 1. Overall Test Execution Flow

```mermaid
stateDiagram-v2
    [*] --> Initialize
    Initialize --> ConfigSetup
    ConfigSetup --> ReportSetup
    ReportSetup --> TestDiscovery
    TestDiscovery --> TestExecution
    
    TestExecution --> APIRequest
    APIRequest --> APIResponse
    APIResponse --> ResponseValidation
    
    ResponseValidation --> StatusCodeCheck
    StatusCodeCheck --> HeaderVerification
    HeaderVerification --> ResponseBodyValidation
    ResponseBodyValidation --> JSONStructureCheck
    
    JSONStructureCheck --> TestPass: All Checks Pass
    StatusCodeCheck --> TestFail: Status Code Mismatch
    HeaderVerification --> TestFail: Header Mismatch
    ResponseBodyValidation --> TestFail: Body Validation Failed
    JSONStructureCheck --> TestFail: JSON Structure Invalid
    
    TestPass --> ReportGeneration
    TestFail --> ReportGeneration
    
    ReportGeneration --> ReportStorage
    ReportStorage --> [*]
```

### Flow Description:
1. **Initialize**: Load pytest configuration and environment variables
2. **ConfigSetup**: Setup API constants, base URLs, and test markers
3. **ReportSetup**: Create timestamp-based report file
4. **TestDiscovery**: Pytest discovers all test cases from test files
5. **TestExecution**: Execute each test case sequentially
6. **APIRequest**: Make API call using the requests wrapper
7. **APIResponse**: Receive and parse API response
8. **ResponseValidation**: Validate all response attributes
9. **TestResult**: Mark as Pass or Fail based on validations
10. **ReportGeneration**: Generate HTML report with results
11. **ReportStorage**: Store report with timestamp

---

## 2. API Request & Response Cycle

```mermaid
stateDiagram-v2
    [*] --> PrepareRequest
    
    PrepareRequest --> FetchURL
    FetchURL --> FetchHeaders
    FetchHeaders --> FetchAuth
    
    FetchAuth --> RequestWrapper
    RequestWrapper --> ExecuteRequest
    
    ExecuteRequest --> ServerProcessing
    ServerProcessing --> APIResponse
    
    APIResponse --> StatusCode
    StatusCode --> ResponseHeaders
    ResponseHeaders --> ResponseBody
    
    ResponseBody --> ParseJSON: JSON Response
    ResponseBody --> TextResponse: Text/HTML Response
    
    ParseJSON --> ResponseReady
    TextResponse --> ResponseReady
    
    ResponseReady --> ReturnResponse
    ReturnResponse --> [*]
```

### API Request Components:
- **URL**: Constructed from `APIConstants` class (e.g., `/search_employee/`, `/employee_details/{code}`)
- **Auth**: Optional authentication (currently None for testing)
- **Headers**: Optional custom headers (Content-Type, etc.)
- **Method**: GET, POST, PATCH, PUT, DELETE (wrapper supports all)

### Response Handling:
- **Status Code**: HTTP response code (expected: 200, 400, 404, etc.)
- **Headers**: Response headers validation (Content-Type, etc.)
- **Body**: Raw response content
- **JSON Parsing**: Automatic parsing if `in_json=True` parameter is set

---

## 3. Test Verification Flow

```mermaid
stateDiagram-v2
    [*] --> ReceiveResponse
    
    ReceiveResponse --> StatusCodeVerification
    
    StatusCodeVerification --> CodeMatch: Code == Expected
    StatusCodeVerification --> CodeMismatch: Code != Expected
    
    CodeMatch --> HeaderVerification
    CodeMismatch --> LogError
    
    HeaderVerification --> HeaderMatch: Header Found
    HeaderVerification --> HeaderMismatch: Header Missing
    
    HeaderMatch --> ResponseKeyVerification
    HeaderMismatch --> LogError
    
    ResponseKeyVerification --> KeyExists: Key in Response
    ResponseKeyVerification --> KeyMissing: Key Not Found
    
    KeyExists --> JSONNullCheck
    KeyMissing --> LogError
    
    JSONNullCheck --> NotNull: Value Not Null
    JSONNullCheck --> IsNull: Value is Null/Empty
    
    NotNull --> DataValidation
    IsNull --> LogError
    
    DataValidation --> CustomChecks
    CustomChecks --> AllPass: All Validations Pass
    CustomChecks --> Failed: Validation Failed
    
    AllPass --> TestAssertPass
    LogError --> TestAssertFail
    Failed --> TestAssertFail
    
    TestAssertPass --> [*]
    TestAssertFail --> [*]
```

### Verification Types:

#### 1. **HTTP Status Code Verification**
```python
verify_http_status_code(response, expected_code)
# Asserts: response.status_code == expected_code
```

#### 2. **Response Header Verification**
```python
verify_response_header(response, header_name, expected_value)
# Asserts: response.headers.get(header_name) == expected_value
```

#### 3. **Response Key Verification**
```python
verify_response_key(actual_value, expected_value, key_name)
# Asserts: actual_value == expected_value
```

#### 4. **JSON Null Check**
```python
verify_json_key_not_null(key, key_name)
# Asserts: key is not None and key != ""
```

#### 5. **Numeric Value Verification**
```python
verify_json_key_gr_zero(key, key_name)
# Asserts: key > 0
```

---

## 4. Complete Test Execution State Machine

```mermaid
stateDiagram-v2
    [*] --> TestSetup
    
    TestSetup --> GetAPIURL
    GetAPIURL --> ConstructHeaders
    ConstructHeaders --> MakeRequest
    
    MakeRequest --> RequestSent
    RequestSent --> WaitForResponse
    
    WaitForResponse --> ResponseReceived: Response OK
    WaitForResponse --> RequestTimeout: Timeout
    WaitForResponse --> NetworkError: Connection Error
    
    RequestTimeout --> HandleError
    NetworkError --> HandleError
    HandleError --> TestFail
    
    ResponseReceived --> ExtractResponse
    ExtractResponse --> CheckStatus
    
    CheckStatus --> Status200: 200 OK
    CheckStatus --> Status400: 400+ Error
    
    Status400 --> TestFail
    
    Status200 --> ParseJSON
    ParseJSON --> ValidateStructure
    
    ValidateStructure --> CheckKeys
    CheckKeys --> ValidateData
    
    ValidateData --> AllValid: Data Valid
    ValidateData --> InvalidData: Data Invalid
    
    InvalidData --> TestFail
    
    AllValid --> LogResults
    LogResults --> TestPass
    
    TestPass --> GenerateReport
    TestFail --> GenerateReport
    
    GenerateReport --> StoreReport
    StoreReport --> [*]
```

---

## 5. Test Case Structure & Flow

Each test case follows this pattern:

```mermaid
graph TD
    A["Test Class Initialized<br/>(TestGetSearchEmployeeData)"] --> B["Test Method Executed<br/>(@pytest.mark)"]
    B --> C["Logger Initialized"]
    C --> D["API Request Made<br/>(get_request)"]
    D --> E["Response Received<br/>(response, response_json)"]
    E --> F["Verification 1:<br/>Status Code Check"]
    F --> G["Verification 2:<br/>Header Check"]
    G --> H["Verification 3:<br/>Response Key Check"]
    H --> I["Verification 4:<br/>Null/Empty Check"]
    I --> J["Verification 5:<br/>Custom Data Check"]
    J --> K["Log Results"]
    K --> L["Test Complete"]
    L --> M["Report Updated"]
```

---

## 6. API Constants & URL Construction Flow

```mermaid
stateDiagram-v2
    [*] --> APIConstants
    
    APIConstants --> SetBaseURL
    SetBaseURL --> URLReady: base_url = http://training.alignedautomation.com:8009
    
    URLReady --> SelectAPI
    
    SelectAPI --> Search: /search_employee/
    SelectAPI --> EmployeeDetails: /employee_details/{code}
    SelectAPI --> Experience: /get_work_and_education_experience/{code}
    SelectAPI --> Manager: /get_reporting_manager_details/{code}
    SelectAPI --> Skills: /get_employee_skill_data/{code}
    SelectAPI --> Performance: /get_performance_rating/{code}
    SelectAPI --> Projects: /project_details/ or /projects/
    SelectAPI --> Attendance: /attendance/
    SelectAPI --> Certificates: /certificates/
    SelectAPI --> Associates: /associates_under_manager/
    
    Search --> ConstructURL
    EmployeeDetails --> ConstructURL
    Experience --> ConstructURL
    Manager --> ConstructURL
    Skills --> ConstructURL
    Performance --> ConstructURL
    Projects --> ConstructURL
    Attendance --> ConstructURL
    Certificates --> ConstructURL
    Associates --> ConstructURL
    
    ConstructURL --> FinalURL
    FinalURL --> [*]
```

### Supported APIs:
| API | Endpoint | Method | Parameters |
|-----|----------|--------|------------|
| Search Employee | `/search_employee/` | GET | None |
| Employee Details | `/employee_details/{code}` | GET | employee_code |
| Work Experience | `/get_work_and_education_experience/{code}` | GET | employee_code |
| Reporting Manager | `/get_reporting_manager_details/{code}` | GET | employee_code |
| Employee Skills | `/get_employee_skill_data/{code}` | GET | employee_code |
| Performance Rating | `/get_performance_rating/{code}` | GET | employee_code |
| Project Details | `/project_details/` | GET | employee_code (optional) |
| Projects | `/projects/` | GET | None |
| Attendance | `/attendance/` | GET | None |
| Certificates | `/certificates/` | GET | employee_code (optional) |
| Associates | `/associates_under_manager/` | GET | employee_code (optional) |

---

## 7. Report Generation Flow

```mermaid
stateDiagram-v2
    [*] --> TestsComplete
    
    TestsComplete --> GatherResults
    GatherResults --> CreateTimestamp
    
    CreateTimestamp --> GenerateName
    GenerateName --> NameFormat: report_YYYY-MM-DD_HH-MM-SS.html
    
    NameFormat --> CreateReportFile
    CreateReportFile --> EmbedStyles
    EmbedStyles --> EmbedScripts
    
    EmbedScripts --> PopulateResults
    PopulateResults --> AddTestDetails
    AddTestDetails --> AddPassFailStats
    
    AddPassFailStats --> GenerateHTML
    GenerateHTML --> SelfContainedHTML
    
    SelfContainedHTML --> StoreInReportsDir
    StoreInReportsDir --> ReportReady: reports/report_YYYY-MM-DD_HH-MM-SS.html
    
    ReportReady --> [*]
```

### Report Details:
- **Location**: `reports/` folder
- **Naming**: `report_YYYY-MM-DD_HH-MM-SS.html`
- **Format**: Self-contained HTML (all CSS/JS embedded)
- **Contents**:
  - Test summary (total, passed, failed)
  - Individual test results
  - Test duration
  - Error messages and stack traces
  - Response details (for debugging)

---

## 8. Project File Structure & Data Flow

```mermaid
graph TD
    A["conftest.py<br/>(Test Configuration)"] --> B["pytest.ini<br/>(Markers & Config)"]
    
    B --> C["src/constants/<br/>api_constants.py"]
    C --> D["API URLs & BaseURL"]
    
    E["src/helpers/<br/>api_requests_wrapper.py"] --> F["HTTP Methods:<br/>GET, POST, etc."]
    
    G["src/helpers/<br/>common_verification.py"] --> H["Assertion Methods:<br/>Status, Headers, JSON"]
    
    I["src/tests/<br/>test_*.py"] --> J["Test Cases"]
    
    D --> J
    F --> J
    H --> J
    
    J --> K["Logger:<br/>src/logger.py"]
    K --> L["Console & File Logs"]
    
    J --> M["Report Generation<br/>conftest.py hook"]
    M --> N["reports/<br/>report_*.html"]
    
    O["src/resources/<br/>testdata.csv"] -.-> J
    P["src/utils/<br/>utils.py"] -.-> J
```

---

## 9. Error Handling Flow

```mermaid
stateDiagram-v2
    [*] --> APICall
    
    APICall --> Success: Response 200-299
    APICall --> ClientError: Response 400-499
    APICall --> ServerError: Response 500-599
    APICall --> Exception: Network/Connection Error
    
    Success --> ProcessResponse
    ProcessResponse --> Validate
    
    ClientError --> LogError: Log Client Error
    ServerError --> LogError: Log Server Error
    Exception --> LogError: Log Exception
    
    LogError --> TestFail
    
    Validate --> ValidationPass: All Pass
    Validate --> ValidationFail: Assertion Fails
    
    ValidationPass --> TestPass
    ValidationFail --> LogFailure
    LogFailure --> TestFail
    
    TestPass --> [*]
    TestFail --> [*]
```

### Error Scenarios:
1. **Connection Error**: Network unreachable, DNS failure
2. **Timeout**: Request exceeds timeout threshold
3. **Client Error (4xx)**: Bad request, unauthorized, not found, etc.
4. **Server Error (5xx)**: Internal server error, service unavailable
5. **Validation Error**: Response doesn't match expected values
6. **JSON Parse Error**: Invalid JSON in response

---

## 10. Data Flow Between Components

```mermaid
graph LR
    A["Test Case"] -->|"Step 1: Get URL"| B["APIConstants"]
    B -->|"Return URL"| A
    
    A -->|"Step 2: Make Request"| C["api_requests_wrapper"]
    C -->|"HTTP Request"| D["HR Portal API Server"]
    D -->|"HTTP Response"| C
    C -->|"Return response + JSON"| A
    
    A -->|"Step 3: Verify"| E["common_verification"]
    E -->|"Assert Result"| A
    
    A -->|"Step 4: Log"| F["logger.py"]
    F -->|"Write Logs"| G["Console & Log Files"]
    
    A -->|"Step 5: Result"| H["conftest.py Hook"]
    H -->|"Collect Result"| I["Report Generator"]
    I -->|"Generate HTML"| J["reports/report_*.html"]
```

---

## 11. Test Execution Sequence Diagram

```mermaid
sequenceDiagram
    participant TC as Test Case
    participant APW as API Wrapper
    participant Server as HR Portal Server
    participant CV as Verification
    participant Report as Report Gen
    
    TC->>APW: 1. Call get_request(url, headers, auth, in_json=True)
    APW->>Server: 2. Send HTTP GET Request
    Server-->>APW: 3. Return Response
    APW->>APW: 4. Parse JSON (if in_json=True)
    APW-->>TC: 5. Return (response, response_json)
    
    TC->>CV: 6. verify_http_status_code(response, 200)
    CV-->>TC: 7. Assert Pass/Fail
    
    TC->>CV: 8. verify_response_header(response, header, value)
    CV-->>TC: 9. Assert Pass/Fail
    
    TC->>CV: 10. verify_response_key(actual, expected)
    CV-->>TC: 11. Assert Pass/Fail
    
    TC->>CV: 12. verify_json_key_not_null(key)
    CV-->>TC: 13. Assert Pass/Fail
    
    TC->>Report: 14. Test Complete (Pass/Fail)
    Report->>Report: 15. Generate HTML Report
    Report-->>TC: 16. Report Stored
```

---

## 12. Key Components Summary

### **conftest.py** (Configuration)
- Configures pytest with dynamic report naming
- Creates timestamped report files
- Sets up report directory

### **api_constants.py** (API Configuration)
- Defines base URL: `http://training.alignedautomation.com:8009`
- Defines all API endpoint URLs
- Default employee code: `AASPL-1918`

### **api_requests_wrapper.py** (HTTP Wrapper)
- Provides `get_request()` method
- Supports optional JSON parsing
- Returns tuple of (response, response_json)

### **common_verification.py** (Assertions)
- `verify_http_status_code()`: Status validation
- `verify_response_header()`: Header validation
- `verify_response_key()`: Key-value validation
- `verify_json_key_not_null()`: Null checks
- `verify_json_key_gr_zero()`: Numeric validation

### **Test Cases** (test_*.py)
- Import required modules
- Create test class with pytest markers
- Define test methods
- Call API -> Get Response -> Verify -> Log

### **logger.py** (Logging)
- Provides structured logging
- Logs test execution flow
- Captures API responses and results

### **pytest.ini** (Markers)
- Defines pytest markers for test categorization
- Enables running tests by marker: `pytest -m Get_Search_Employee_Data`

---

## 13. Execution Commands

```bash
# Run all tests
pytest --html=reports/report.html --self-contained-html

# Run tests by marker
pytest -m Get_Search_Employee_Data --html=reports/report.html --self-contained-html

# Run specific test file
pytest src/tests/Training_Aligned_Automation_TestCases/01_Get_Search_Employee_Data_test.py --html=reports/report.html --self-contained-html

# Run with verbose output
pytest -v --html=reports/report.html --self-contained-html

# Run with logging
pytest -v -s --html=reports/report.html --self-contained-html
```

---

## Summary

The HR Portal API Automation framework follows a structured, modular approach:

1. **Configuration** (conftest.py, pytest.ini) sets up the test environment
2. **Constants** (api_constants.py) provide centralized API configuration
3. **Wrappers** (api_requests_wrapper.py) abstract HTTP complexity
4. **Verification** (common_verification.py) standardizes assertions
5. **Tests** (test_*.py) implement specific test scenarios
6. **Logging** (logger.py) tracks execution
7. **Reporting** (conftest.py hooks) generates timestamped HTML reports

Each test follows the **Arrange-Act-Assert** pattern:
- **Arrange**: Get API URL and prepare headers
- **Act**: Make API request via wrapper
- **Assert**: Verify response using common verification methods
- **Report**: Generate timestamped HTML report with results

