fotocasa_keywords ={
    # 'sequence': ['base_url', 'property', 'province', 'price', 'bedroom', 'bathroom', 'size', 'dwelling', 'location','identifier','extras','equipment', 'pet'],    
    
    'base_url': 'https://www.fotocasa.es/es/alquiler/',
    'property':{
        'dwelling': 'casas/',
        'local': 'locales/'
    },
    'province': {
        'madrid': 'madrid-provincia/todas-las-zonas/l?gridType=list&sortType=publicationDate',
        'barcelona': 'barcelona-provincia/todas-las-zonas/l?gridType=list&sortType=publicationDate'
    },
    'minimumPrice': '&minPrice={}',
    'maximumPrice': '&maxPrice={}',
    'bedroom': {
        'one': '&minRooms=1',
        'two': '&minRooms=2',
        'three': '&minRooms=3',
        'four': '&minRooms=4'
    },
    'bathroom': {
        'one': '&minBathrooms=1',
        'two': '&minBathrooms=2',
        'three': '&minBathrooms=3'
    },
    'dwelling': {
        'loft': '&propertySubtypeIds=8',
        'studio': '&propertySubtypeIds=54',

        'flat': '&propertySubtypeIds=2;1',
        'apartment': '&propertySubtypeIds=2;1',

        'duplex': '&propertySubtypeIds=4',

        'penthouse': '&propertySubtypeIds=6',
        
        'townhouse': '&propertySubtypeIds=7',
        'house': '&propertySubtypeIds=3;5;9',
    },
    'city':{
        'hospitalet': '&combinedLocationIds=724,9,8,232,375,8101,0,0,0', 
    },
    'district': {
        'les_corts': '&combinedLocationIds=724,9,8,232,376,8019,0,1148,0',
        'sarria_sant_gervasi': '&combinedLocationIds=724,9,8,232,376,8019,0,1143,0',
        'gracia': '&combinedLocationIds=724,9,8,232,376,8019,0,1150,0',
        'horta_ginardo': '&combinedLocationIds=724,9,8,232,376,8019,0,1149,0',
        'nou_barris': '&combinedLocationIds=724,9,8,232,376,8019,0,1147,0',
        'sant_andreu': '&combinedLocationIds=724,9,8,232,376,8019,0,1146,0',
        'sant_marti': '&combinedLocationIds=724,9,8,232,376,8019,0,1145,0',
        'eixample': '&combinedLocationIds=724,9,8,232,376,8019,0,1151,0',
        'ciutat_vella': '&combinedLocationIds=724,9,8,232,376,8019,0,1152,0',
        'sants_montjuic': '&combinedLocationIds=724,9,8,232,376,8019,0,1144,0',
        'surroundings_of_barcelona': '&combinedLocationIds=724,9,8,0,0,0,0,0,0',
        'arganzuelas': '&combinedLocationIds=724,14,28,173,0,28079,0,671,0',
        'barajas': '&combinedLocationIds=724,14,28,173,0,28079,0,668,0',
        'carabanchel': '&combinedLocationIds=724,14,28,173,0,28079,0,171,0',
        'centro': '&combinedLocationIds=724,14,28,173,0,28079,0,672,0',
        'chamartin': '&combinedLocationIds=724,14,28,173,0,28079,0,176,0',
        'ciudad_lineal': '&combinedLocationIds=724,14,28,173,0,28079,0,685,0',
        'fuencarral_el_pardo': '&combinedLocationIds=724,14,28,173,0,28079,0,187,0',
        'hortaleza': '&combinedLocationIds=724,14,28,173,0,28079,0,678,0',
        'latina': '&combinedLocationIds=724,14,28,173,0,28079,0,675,0',
        'moncloa_aravaca': '&combinedLocationIds=724,14,28,173,0,28079,0,669,0',
        'moratalaz': '&combinedLocationIds=724,14,28,173,0,28079,0,191,0',
        'puente_de_vallecas': '&combinedLocationIds=724,14,28,173,0,28079,0,677,0',
        'retiro': '&combinedLocationIds=724,14,28,173,0,28079,0,199,0',
        'salamanca': '&combinedLocationIds=724,14,28,173,0,28079,0,667,0',
        'san_blas': '&combinedLocationIds=724,14,28,173,0,28079,0,676,0',
        'tetuan': '&combinedLocationIds=724,14,28,173,0,28079,0,681,0',
        'usera': '&combinedLocationIds=724,14,28,173,0,28079,0,205,0',
        'vicalvaro': '&combinedLocationIds=724,14,28,173,0,28079,0,209,0',
        'villa_de_vallecas': '&combinedLocationIds=724,14,28,173,0,28079,0,680,0',
        'villaverde': '&combinedLocationIds=724,14,28,173,0,28079,0,670,0',
        'surroundings_of_madrid': '&combinedLocationIds=724,14,28,0,0,0,0,0,0',
    },
    'extraFilter': {
        'elevator': '&featureIds=13',
        'parking': '&featureIds=5',
        'swimming_pool': '&featureIds=17',
        'balcony': '&featureIds=10',
        'terrace_or_patio': '&featureIds=10',
        'storage_room': '&featureIds=11',
    },
    'equipment': {
        'not_furnished': '&featureIds=130',
        'furnished': '&featureIds=19',
   },
   'pet':{
       True: '&featureIds=49',
       False: ''
    }
}
