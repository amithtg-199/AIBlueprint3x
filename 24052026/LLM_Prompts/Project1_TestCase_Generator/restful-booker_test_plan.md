# Restful Booker API Test Plan

## 1. Document References
- `API-booker-test-PRD.pdf`
- `Restful-booker_API_Spec.pdf`
- `prompt.md`
- API Specification URL: `https://restful-booker.herokuapp.com/apidoc/index.html`

## 2. Objective
Validate the Restful Booker API end-to-end through enterprise-grade functional and non-functional test coverage. The test plan is derived strictly from the PRD scope and the API documentation provided by the Spec.

## 3. System Under Test
- API Base URL: `https://restful-booker.herokuapp.com`
- Key endpoints covered:
  - `POST /auth`
  - `POST /booking`
  - `GET /booking`
  - `GET /booking/{id}`
  - `PUT /booking/{id}`
  - `PATCH /booking/{id}`
  - `DELETE /booking/{id}`
  - `GET /ping`

## 4. Scope
### 4.1 Functional Scope
This plan addresses the PRD functional requirements for:
- Create booking operations
- Read booking operations
- Update booking operations
- Delete booking operations
- Authentication and authorization mechanisms
- Query and filter behavior for read endpoints
- Data validation and error handling

### 4.2 Non-Functional Scope
This plan addresses the PRD non-functional requirements for:
- Performance measurement
- Throughput and load observation
- Concurrency behavior
- Security and HTTPS enforcement
- Rate limiting behavior
- Availability / health check
- Backup and recovery measurement attempt

## 5. Test Strategy
### 5.1 Functional Testing
- Verify correctness and compliance of CRUD endpoints with the Spec.
- Validate payload structure, required fields, and response data.
- Include positive and negative test cases.
- Ensure authorization is enforced for protected operations.

### 5.2 Non-Functional Testing
- Use measurement-only test cases when no explicit SLA or limit is documented.
- Record metrics for response time, throughput, load behavior, and concurrency.
- Verify security artifacts such as HTTPS enforcement and authorization control.
- Document any inability to proceed when the Spec lacks operational details.

## 6. Test Coverage Summary
### 6.1 Functional Coverage
- Auth token creation
- Booking creation with valid data
- Booking creation with missing mandatory fields
- Booking creation with invalid date format
- Booking retrieval by ID
- Booking retrieval for non-existent ID
- Query-based booking search
- Booking update with valid auth
- Booking update without auth
- Booking deletion with auth

### 6.2 Non-Functional Coverage
- GET booking response time measurement
- POST booking response time measurement
- Sustained throughput measurement
- Sustained load measurement
- Stress ramp measurement
- Concurrent CRUD behavior measurement
- Rate limiting behavior observation
- Health check availability measurement
- HTTPS/TLS enforcement measurement
- Authorization enforcement measurement for PUT/DELETE
- Backup and recovery measurement attempt

## 7. Traceability to PRD
| PRD Scope | Test Artifacts | Covered By |
|---|---|---|
| Functional Testing | `Functional_Test_Cases.csv` | Create, Read, Update, Delete, Auth, Error Handling |
| Data Validation Testing | `Functional_Test_Cases.csv` | Invalid payload, missing fields, date validation |
| Error Handling Testing | `Functional_Test_Cases.csv` | Invalid ID, unauthorized access, malformed inputs |
| Performance Testing | `NonFunctional_Test_Cases.csv` | Response time, throughput, load, stress |
| Security Testing | `NonFunctional_Test_Cases.csv` | HTTPS enforcement, auth enforcement |
| Load Testing | `NonFunctional_Test_Cases.csv` | Sustained load, stress ramp |
| Concurrency Testing | `NonFunctional_Test_Cases.csv` | Concurrent CRUD behavior |
| Rate Limiting Testing | `NonFunctional_Test_Cases.csv` | High request-rate observation |
| Backup and Recovery Testing | `NonFunctional_Test_Cases.csv` | Measurement attempt; insufficient Spec details |

## 8. Test Artifacts
- `Functional_Test_Cases.csv`
- `NonFunctional_Test_Cases.csv`

## 9. Constraints and Assumptions
- No new features or requirements are added beyond the PRD.
- Test cases are based only on the PRD and the provided API Spec.
- Where the Spec lacks explicit operational details (e.g., backup/recovery, documented rate limits), the related test case is marked as measurement-only or as insufficient information.
- The CSV files contain the formal test cases and expected results.

## 10. Execution Approach
- Execute functional cases through Postman, REST Assured, or equivalent API test tools.
- Execute non-functional measurement cases using load/test tooling to capture metrics rather than enforce thresholds.
- Log actual results, status, and observations directly in the CSV artifacts.

## 11. Notes
- The health endpoint `GET /ping` is included for availability measurement.
- Authorization for PUT and DELETE is validated using the token endpoint and the cookie/header methods described in the Spec.
- This test plan intentionally avoids assumptions beyond the documented API behavior.
