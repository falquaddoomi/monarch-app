from fastapi import APIRouter, Depends
from monarch_api.additional_models import PaginationParams

from monarch_api.utils.get_similarity import *

router = APIRouter(
    prefix="/api/semsim",
    tags=["semsim"],
    responses = {
        404: {"description":"Not Found"}
    }
)

@router.get("/semsim/{subjlist}/{objlist}")
async def _get_termlist_similarity(
    pagination: PaginationParams = Depends(),
    subjlist: str = "",
    objlist: str = "",
    predicate: str = "i,p",
):
    results = termlist_similarity(
        subjlist=subjlist,
        objlist=objlist,
        predicate=predicate,
        offset=pagination.offset,
        limit=pagination.limit,
    )
    return results
