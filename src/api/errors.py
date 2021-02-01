class InternalServerError(Exception):
    pass


class GroupNotExistsError(Exception):
    def __init__(self, group_id):
        self.group_id = group_id

class GroupValidationError(Exception):
    def __init__(self, invalid_jobs):
        self.invalid_jobs = invalid_jobs


class JobNotExistsError(Exception):
    def __init__(self, job_id):
        self.job_id = job_id


class JobDefinitionNotExistsError(Exception):
    def __init__(self, job_id):
        self.job_id = job_id


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "GroupNotExistsError": {
        "message": "Group with given id doesn't exists : ",
        "status": 400
    },
    "GroupValidationError": {
        "message": "Group with given jobs do not exists : ",
        "status": 400
    },
    "JobNotExistsError": {
        "message": "Job with given id doesn't exists : ",
        "status": 400
    },
    "JobDefinitionNotExistsError": {
        "message": "Job definition doesn't exists : ",
        "status": 400
    }
}
