idealista_keywords ={
    # 'pattern': [
    #     'base_url', 'property', 'district', 'price_min','price_max', 'dwelling', 
    #     'bedroom',  'bathroom', 'equipment', 'extras', 'pet', 'criteria_sort'
    # ],
    'base_url': 'https://www.idealista.com/',
    'property': {
        'dwelling': 'alquiler-viviendas/',
        'local': 'alquiler-locales/',
    },
    'city':{
        'hospitalet': 'barcelona/hospitalet/'
    },
    'district':{
        'les_corts': 'barcelona/les-corts/',
        'sarria_sant_gervasi': 'barcelona/sarria-sant-gervasi/',
        'gracia': 'barcelona/gracia/',
        'horta_ginardo': 'barcelona/horta-guinardo/',
        'nou_barris': 'barcelona/nou-barris/',
        'sant_andreu': 'barcelona/sant-andreu/',
        'sant_marti': 'barcelona/sant-marti/',
        'eixample': 'barcelona/eixample/',
        'ciutat_vella': 'barcelona/ciutat-vella/',
        'sants_montjuic': 'barcelona/sants-montjuic/',
        'surroundings_of_barcelona': '/barcelona-provincia/',
        'arganzuelas': 'madrid/arganzuela/',
        'barajas': 'madrid/barajas/',
        'carabanchel': 'madrid/carabanchel/',
        'centro': 'madrid/centro/',
        'chamartin': 'madrid/chamartin/',
        'ciudad_lineal': 'madrid/ciudad-lineal/',
        'fuencarral_el_pardo': 'madrid/fuencarral/el-pardo/',
        'hortaleza': 'madrid/hortaleza/',
        'latina': 'madrid/latina/',
        'moncloa_aravaca': 'madrid/moncloa/aravaca/',
        'moratalaz': 'madrid/moratalaz/',
        'puente_de_vallecas': 'madrid/puente-de-vallecas/',
        'retiro': 'madrid/retiro/',
        'salamanca': 'madrid/salamanca/',
        'san_blas': 'madrid/san-blas/',
        'tetuan': 'madrid/tetuan/',
        'usera': 'madrid/usera/',
        'vicalvaro': 'madrid/vicalvaro/',
        'villa_de_vallecas': 'madrid/villa-de-vallecas/',
        'villaverde': 'madrid/villaverde/',
        'surroundings_of_madrid': 'madrid-provincia/',
    },
    'key': 'con-',
    'maximumPrice': 'precio-hasta_{},',
    'minimumPrice': 'precio-desde_{},',
    'dwelling': {
        'loft': 'estudios,',
        'studio': 'estudios,',
        'flat': 'pisos,',
        'apartment': 'pisos,',
        'duplex': 'duplex,',
        'penthouse': 'aticos,',
        'townhouse': 'chalets,',
        'house': 'chalets,',
        'rural_property': 'casas-de-pueblo,'
    },
    'bedroom': {
        'one': 'de-un-dormitorio,',
        'two': 'de-dos-dormitorios,',
        'three': 'de-tres-dormitorios,',
        'four': 'de-cuatro-cinco-habitaciones-o-mas,'
    },
    'bathroom': {
        'one': 'un-bano,dos-banos,tres-banos-o-mas,',
        'two': 'dos-banos,tres-banos-o-mas,',
        'three': 'tres-banos-o-mas,'
    },
    'equipment': {
        'not_furnished': 'amueblado_solo-cocina-equipada,',
        'furnished': 'amueblado_amueblados,',
    },
    'extraFilter': {
        'elevator': 'ascensor,',
        'parking': 'garaje,',
        'swimming_pool': 'piscina,',
        'balcony': 'terraza,',
        'terrace_or_patio': 'terraza,',
        'storage_room': 'trastero,',
        'air_conditioning': 'aireacondicionado,',
        'wardrobe': 'armarios-empotrados,',
        'garden': 'jardin,'
    },
    'pet':{
        True: 'mascotas,',
        False: ''
    } ,
    'criteria_sort': 'publicado_ultimas-24-horas/?ordenado-por=fecha-publicacion-desc'

    # 'publication_date': {
    #     'last_24_hours': 'publicado_ultimas-24-horas',
    #     'last_week': 'publicado_ultima-semana',
    #     'last_month': 'publicado_ultimo-mes'
    # },

    # },
    # 'floor': {
    #     'top': 'con-ultimas-plantas',
    #     'mid': 'plantas-intermedias',
    #     'ground': 'solo-bajos'
    # },
    # 'state': {
    #     'new': 'con-obra-nueva',
    #     'old': 'para-reformar',
    #     'good': 'buen-estado'
    # },
    # 'criteria_sort': {
    #     'price_asc': '?ordenado-por=precio-asc',
    #     'price_desc': '?ordenado-por=precio-desc',
    #     'publ_date_asc': '?ordenado-por=fecha-publicacion-asc',
    #     'publ_date_desc': '?ordenado-por=fecha-publicacion-desc',
    #     'sales': '?ordenado-por=rebajas-desc',
    #     'price_floor_asc': '?ordenado-por=precio-metro-cuadrado-asc',
    #     'price_floor_desc': '?ordenado-por=precio-metro-cuadrado-desc',
    #     'area_asc': '?ordenado-por=area-asc',
    #     'area_desc': '?ordenado-por=area-desc',
    #     'floor_lvl_asc': '?ordenado-por=planta-asc',
    #     'floor_lvl_desc': '?ordenado-por=planta-desc'
    # }

}