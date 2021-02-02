import logging
from flask import jsonify, url_for
from api.errors import *
from api.job import execute_group, celery, setup
from api.validation import Validation

log = logging.getLogger(__name__)
app = setup.get_app()
conf = setup.get_config()
validation = Validation()
port = conf['app']['port']
host = conf['app']['host']


@app.route('/status/<task_id>')
def task_status(task_id):
    try:
        task = celery.AsyncResult(task_id)
        if task.state == "PENDING":
            raise JobNotExistsError(task_id)
        else:
            response = {
                'task_id': task_id,
                'state': task.state,
            }
        return jsonify(response), 200
    except JobNotExistsError as e:
        return errors.get('JobNotExistsError').get('message') + e.job_id, errors.get('JobNotExistsError').get('status')
    except Exception:
        return errors.get('InternalServerError')


@app.route('/group/<group_id>')
def group(group_id):
    try:
        validation.validate_group(group_id)
        validation.validate_group_jobs(group_id)
        result = execute_group.delay(group_id)

        job_ids = []
        while 1:
            if result and result.ready():
                print(result)
                for job in result.children:
                    print(job)
                    job_ids.append(job.task_id)
                break
        job_url = [url_for('task_status', task_id=job_id) for job_id in job_ids]
        return jsonify({'Check job status at': job_url}), 202
    except GroupNotExistsError as e:
        return errors.get('GroupNotExistsError').get('message') + e.group_id, errors.get('GroupNotExistsError').get('status')
    except GroupValidationError as e:
        return errors.get('GroupValidationError').get('message') + str(e.invalid_jobs), errors.get('GroupValidationError').get('status')
    except JobDefinitionNotExistsError as e:
        return errors.get('JobDefinitionNotExistsError').get('message') + e.job_id , errors.get('JobDefinitionNotExistsError').get('status')
    except JobNotExistsError as e:
        return errors.get('JobNotExistsError').get('message') + e.job_id , errors.get('JobNotExistsError').get('status')
    except Exception:
        return errors.get('InternalServerError').get('message'), errors.get('InternalServerError').get('status')


# if __name__ == '__main__':
#     app.run(host=host, port=port)
