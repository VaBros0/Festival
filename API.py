API_KEY = 'e68af0c8-d28f-44ca-9ddb-5e0319b16cda'
BASE_URL = 'https://kinopoiskapiunofficial.tech/api/v2.2/films'

def get_films(query=None, page=1):
    headers = {'X-API-KEY': API_KEY}
    params = {
        'order': 'RATING',
        'ratingFrom': 7,
        'ratingTo': 10,
        'yearFrom': 2015,
        'yearTo': 2025,
        'page': page,
    }

    if query:
        params['keyword'] = query
    
    response = requests.get(BASE_URL, headers=headers, params=params)
    response.encoding = 'utf-8'

    if response.status_code == 200:
        return response.json()['items']
    else:
        return []
