import os

from pydantic import BaseSettings

from monarch_py.implementations.oak.oak_implementation import OakImplementation
from monarch_py.implementations.solr.solr_implementation import SolrImplementation


class Settings(BaseSettings):
    solr_host = os.getenv("SOLR_HOST") if os.getenv("SOLR_HOST") else "127.0.0.1"
    solr_port = os.getenv("SOLR_PORT") if os.getenv("SOLR_PORT") else 8983
    solr_url = os.getenv("SOLR_URL") if os.getenv("SOLR_URL") else f"http://{solr_host}:{solr_port}/solr"


settings = Settings()

solr = SolrImplementation(base_url=settings.solr_url)

oak = OakImplementation()