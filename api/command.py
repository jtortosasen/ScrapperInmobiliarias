async def post_search_criterion(request):
    from api.handler import search_criterion as _search_criterion
    return await _search_criterion(request)

async def post_search_criteria(request):
    from api.handler import search_criteria as _search_criteria
    return await _search_criteria(request)

async def post_api_url(request):
    from api.handler import api_url as _api_url
    return await _api_url(request)

async def get_logging_level(request):
    from api.handler import logging_level as _logging_level
    return await _logging_level(request)

