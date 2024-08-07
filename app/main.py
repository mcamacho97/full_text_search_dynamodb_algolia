import database_manager
import algolia_manager
import json
import logging
import uuid


logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)


def create_response(status_code, message):
    return {
        "status_code": status_code,
        "body": json.dumps(message),
    }

def save_person (event, context, callback):
    person = json.loads(event.body)
    logger.info(person)

    person.personId = uuid.uuid4()

    response = database_manager.save_person(person)
    return create_response(200, response)

def 