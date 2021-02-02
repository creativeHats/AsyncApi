## **Async API**

This module simplifies the triggering of long-running processes by creating RESTful API’s that manage and trigger the
processes.

Since this is a MVP , the configurations and backends are simplified. Scalibilty and optimaztions are discussed further.

- The jobs and groups info is stored in `resources/config.yaml`. The group and jobs are defined as follows
    - One group can have multiple jobs
    - A job represents a long-running process.A long-running process can be system sleep / logging and it may intermittently run
forever to simulate a system failure.
      
      
#### Functionality
-   Endpoint to trigger a group. `/group/<group_name>`
-   Once a group action is triggered, simulate the background process that runs all of
the jobs within that group.
-   The long-running process status can be tracked via endpoint `/status/<job_id>`

The long running operation itself is turned into a resource, created using the original request with a response telling the client where to find the results. The client polls the group request to GET all the child jobs, and will eventually be redirected to another resource representing the job id. Since the output has its own URI, it becomes possible GET it multiple times, as long as it has not been deleted.


The API flow is well depicted in the following diagram

![alt text](images/api_flow.png "Group Job API Flow")

## Usage

### Prerequisites
1. Make sure you have `Docker` installed on the host computer to run and test the application
2. port `5100` is available for rest api
3. port `6379` is available for redis backend

### Setup

#### Building the docker file

Go to the root folder of the project and execute

` docker build .`

This will start building docker images for _redis_ , _flask_ and _celery_

` docker-compose up -d`

The above command should start docker process.

### Use

**Trigger Group**

Enter the following URL `http://localhost:5100/group/group_a` , this will trigger all the jobs under group_a.
The following groups and jobs are configured. please refer to `resources/config.yaml` for more details
    
    -   [Valid] "group_a"  with [Valid] jobs and definition "job_a1" , "job_a2" and "job_a3"
    -   [Valid] "group_b"  with  jobs and [InValid] definition "job_b1" , "job_b2" and "job_b3"
    -   [Valid] "group_c"  with [InValid]  no jobs and [InValid] 

A valid request `http://localhost:5100/group/group_a` should return url for tracking the child jobs in the following format

`{"Check job status at":["/status/78b988f6-87d9-4225-86b5-cabe6e475102","/status/a9f27bc0-e4c1-49d8-9818-851e1388e590","/status/05cd046a-7a20-4711-9dd0-b57cf1028135"]}`


**Check Job Status**

Enter the following URL `http://localhost:5100/status/<job_id>` , this return the job status

Valid Response :

`{"state":"SUCCESS","task_id":"78b988f6-87d9-4225-86b5-cabe6e475102"}`

Invalid Response :

`Job with given id doesn't exists : dummy`

### Running Functional Tests
`cd tests`

`pytest`

### Further Improvements (Scalibilty and optimaztions)
1. The groups and config definition can be moved to a database backend for scalibilty/tracking purposes. This backend can also serve as an audit for the job execution status.
2. Rule based validation of the group and job definitions 
3. A separate backend can be created for `celery` which will enable spawning multiple workers.
4. Configure load balancing for multiple worker execution
