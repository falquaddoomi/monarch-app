from typing import List, Union
from typing_extensions import Annotated

from fastapi import APIRouter, Depends, Query
from monarch_api.additional_models import PaginationParams
from monarch_api.config import settings
from monarch_api.model import AssociationResults
from monarch_py.implementations.solr.solr_implementation import SolrImplementation

router = APIRouter(
    tags=["association"],
    responses={404: {"description": "Not Found"}},
)


@router.get("")
@router.get("/all")
async def _get_associations(
    category: Union[List[str], None] = Query(default=None),
    subject: Union[List[str], None] = Query(default=None),
    predicate: Union[List[str], None] = Query(default=None),
    object: Union[List[str], None] = Query(default=None),
    entity: Union[List[str], None] = Query(default=None),
    direct: Union[bool, None] = Query(default=None),
    pagination: PaginationParams = Depends(),
) -> AssociationResults:
    """Retrieves all associations for a given entity, or between two entities."""

    si = SolrImplementation(base_url=settings.solr_url)
    response = si.get_associations(
        category=category,
        predicate=predicate,
        subject=subject,
        object=object,
        entity=entity,
        direct=direct,
        offset=pagination.offset,
        limit=pagination.limit,
    )

    return response
