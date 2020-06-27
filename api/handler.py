import asyncio
from log.log_config import logger
import logging


async def search_criterion(request):
    try:
        req = await request.json()
        logger.info('load JSON criterion')
        criterion = await _extract_criterion(req)
        logger.debug(f'criterion: {str(criterion)}')
        _search_criterion(criterion)
        return ok()

    except Exception as e:
        logger.exception(e)
        return failure(e)

async def search_criteria(request):
    try:
        req = await request.json()
        logger.info('load JSON criteria')
        criteria = await _extract_criteria(req)
        logger.debug(f'criteria: {criteria}')
        _search_criteria(criteria)
        return ok()

    except Exception as e:
        logger.exception(e)
        return failure(e)

async def api_url(request):
    try:
        req = await request.json()
        _api_url(req['url'])
        return ok()
    except Exception as e:
        logger.exception(e)
        return failure(e)

async def logging_level(request):
    try:
        _logging_level(_parse_logging_level(request.match_info['level']))
        return ok()
    except Exception as e:
        return failure(e)

def parse_json(json_data):
    jid = json_data['id']
    jprovince = json_data['province']['option']
    jproperty =  json_data['property']['option']
    jcity = json_data['city']['option']
    jdistrict =  json_data['district']['option']
    try:
        jmaximumPrice =  int(float(json_data.get('maximumPrice', '')))
    except Exception:
        jmaximumPrice = ''
    try:
        jminimumPrice = int(float(json_data.get('minimumPrice', '')))
    except Exception:
        jminimumPrice = ''
    jbedroom = json_data['bedroom'].get('option', '')
    jbathroom = json_data['bathroom'].get('option', '')
    jextraFilter = [f.get('option', '') for f in json_data['additionalFilters']]
    jdwelling = json_data['dwelling']['option']
    jequipment = json_data['equipment'].get('option', '')
    jpet = json_data.get('allowPet', '')

    return {
        "id": jid,
        "province": jprovince,
        "property": jproperty,
        "city": jcity,
        "district": jdistrict,
        "maximumPrice": jmaximumPrice,
        "minimumPrice": jminimumPrice,
        "bedroom": jbedroom,
        "bathroom": jbathroom,
        "extraFilter": jextraFilter,
        "dwelling": jdwelling,
        "equipment": jequipment,
        "pet": jpet
    }

async def _extract_criterion(json):
    for criterion in json:
        await asyncio.sleep(0)
        if criterion not in static.json_criterion:
            raise Exception(''.join(['Invalid criterion ', criterion]))
    return parse_json(json)

async def _extract_criteria(json):
    criteria = []
    for criterion in json['searchCriteria']:
        c = await _extract_criterion(json=criterion)
        criteria.append(c)
    return criteria

def _parse_logging_level(level):
    return {
        'info': logging.INFO,
        'debug': logging.DEBUG,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL,
    }[level]

from api.response import ok, failure
from api.task import search_criteria as _search_criteria
from api.task import search_criterion as _search_criterion
from api.task import api_url as _api_url
from api.task import logging_level as _logging_level
from api import static