from algoliasearch.search_client import SearchClient
import os
import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

algolia_app_id = os.environ("ALGOLIA_APP_ID")
algolia_admin_api_key = os.environ("ALGOLIA_ADMIN_API_KEY")
algolia_index_name = os.environ("ALGOLIA_INDEX_NAME")

# Connect and authenticate with your Algolia app
client = SearchClient.create(algolia_app_id, algolia_admin_api_key)
index = client.init_index(algolia_index_name)


def prepare_person_for_algolia(stream_person):
    logger.info(stream_person)

    return {
        "personId": stream_person.personId.S,
        "name": stream_person.name.S,
        "country": stream_person.country.S
    }

def add_person(stream_person):
    person = prepare_person_for_algolia(stream_person)
    logger.info(person)

    return index.save_object(person)

def search_person(query):
    return index.search(query)