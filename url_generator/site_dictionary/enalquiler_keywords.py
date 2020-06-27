enalquiler_keywords ={
    # 'sequence' : [
    #     'base_url', 'district', 'min_price', 'max_price', 
    #     'bedroom', 'equipment','dwelling', 'propetary_type',
    #     'bathroom','extraFilter','pet'
    # ],
    'base_url': 'https://www.enalquiler.com/search?fecha=2&',
    'city': {
        'hospitalet': 'provincia=9&poblacion=23880'
    },
    'district': {
        'les_corts': 'provincia=9&poblacion=4596&distritos=5',
        'sarria_sant_gervasi': 'provincia=9&poblacion=4596&distritos=10',
        'gracia': 'provincia=9&poblacion=4596&distritos=3',
        'horta_ginardo': 'provincia=9&poblacion=4596&distritos=4',
        'nou_barris': 'provincia=9&poblacion=4596&distritos=6',
        'sant_andreu': 'provincia=9&poblacion=4596&distritos=7',
        'sant_marti': 'provincia=9&poblacion=4596&distritos=8',
        'eixample': 'provincia=9&poblacion=4596&distritos=2',
        'ciutat_vella': 'provincia=9&poblacion=4596&distritos=1',
        'sants_montjuic': 'provincia=9&poblacion=4596&distritos=9',
        'surroundings_of_barcelona': 'provincia=9',
        'arganzuelas': 'provincia=30&poblacion=27745&distritos=11',
        'barajas': 'provincia=30&poblacion=27745&distritos=12',
        'carabanchel': 'provincia=30&poblacion=27745&distritos=13',
        'centro': 'provincia=30&poblacion=27745&distritos=14',
        'chamartin': 'provincia=30&poblacion=27745&distritos=15',
        'ciudad_lineal': 'provincia=30&poblacion=27745&distritos=17',
        'fuencarral_el_pardo': 'provincia=30&poblacion=27745&distritos=18',
        'hortaleza': 'provincia=30&poblacion=27745&distritos=19',
        'latina': 'provincia=30&poblacion=27745&distritos=20',
        'moncloa_aravaca': 'provincia=30&poblacion=27745&distritos=21',
        'moratalaz': 'provincia=30&poblacion=27745&distritos=22',
        'puente_de_vallecas': 'provincia=30&poblacion=27745&distritos=23',
        'retiro': 'provincia=30&poblacion=27745&distritos=24',
        'salamanca': 'provincia=30&poblacion=27745&distritos=25',
        'san_blas': 'provincia=30&poblacion=27745&distritos=26',
        'tetuan': 'provincia=30&poblacion=27745&distritos=27',
        'usera': 'provincia=30&poblacion=27745&distritos=28',
        'vicalvaro': 'provincia=30&poblacion=27745&distritos=29',
        'villa_de_vallecas': 'provincia=30&poblacion=27745&distritos=30',
        'villaverde': 'provincia=30&poblacion=27745&distritos=31',
        'surroundings_of_madrid': 'provincia=30',
    },
    'minimumPrice': '&precio_min={}',
    'maximumPrice': '&precio_max={}',
    'bedroom': {
        'one': '&habitaciones=1',
        'two': '&habitaciones=2',
        'three': '&habitaciones=3',
        'four': '&habitaciones=4'
    },
    'equipment': {
        'not_furnished': '&amueblado=2',
        'furnished': '&amueblado=1',
   },
    'dwelling': {
        'loft': '&tipo=5',
        'studio': '&tipo=6',
        'flat': '&tipo=2',
        'apartment': '&tipo=2',
        'duplex': '&tipo=4',
        'penthouse': '&tipo=3',
        'townhouse': '&tipo=7',
        'house': '&tipo=7',
    },
    # 'propetary_type': {
    #     'particular':  '&tipo_usuario=1',
    #     'agency': ' &tipo_usuario=2'
    # },
    'bathroom': {
        'one': '&banos=1',
        'two': '&banos=2',
        'three': '&banos=3'
    },
    'extraFilter':{
        'elevator': '&ascensor=1',
        'parking': '&garaje_incluido=1',
        'patio': '&exterior=1',
        'swimming_pool': '&piscina=1',
        'terrace': '&terraza=1',
    },
    'pet': {
        True: '&acepta_animales=1',
        False: '',
    },
    'sort': '&order_field=1'
}