from api.errors import *
from setup import Setup


class Validation:
    config = None

    def __init__(self):
        if not self.config:
            self.config = Setup().get_config()

    def validate_job(self, job_name):
        try:
            self.config['job'][job_name]
        except KeyError:
            raise JobDefinitionNotExistsError(job_name)
        return True

    def validate_group(self, group_name):
        try:
            self.config['group'][group_name]
        except KeyError:
            raise GroupNotExistsError(group_name)
        return True

    def validate_group_jobs(self, group_name):
        g_def = self.config['group'][group_name]
        invalid_jobs = []
        for job in g_def:
            try:
                self.validate_job(job)
            except JobDefinitionNotExistsError:
                invalid_jobs.append(job)
        if invalid_jobs:
            raise GroupValidationError(invalid_jobs)
        return True
