def setup_routes(app):
    from api.command import post_search_criterion
    from api.command import post_search_criteria
    from api.command import post_api_url
    from api.command import get_logging_level

    app.router.add_post('/api/searchCriterion', post_search_criterion)
    app.router.add_post('/api/searchCriteria', post_search_criteria)
    app.router.add_post('/api/apiUrl', post_api_url)
    app.router.add_get('/api/loggingLevel/{level}', get_logging_level)

