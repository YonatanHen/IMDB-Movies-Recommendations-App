
'''
This function create an endpoint with the search parameters entered by the user. 
The dictionary value has been copied from imdb.
'''
def createFilters(filters):        
        release_year = None

        if 'release_year' in filters:
            release_year_filters = filters['release_year']
            if len(filters['release_year']) == 1:
                    release_year_filter = release_year_filters[0]
                    release_year = f"release_date={release_year_filter}-01-01,{release_year_filter}-12-31"
            else:
                    release_year = f"release_date={release_year_filters[0]}-01-01,{release_year_filters[1]}-12-31"
                
        endpoint = "" if not release_year else "&"+release_year
        filters.pop('release_year')
        print(filters)
        for key,value in filters.items():
               value = value.replace(' ', '%20') 
               endpoint += "&"+key+"="+value

        return endpoint

        