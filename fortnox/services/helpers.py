def collect_all_items_from_paginators(self: object, params: dict, url: str, targeted_service: str) -> list:
    '''
    Returns all items from paginated response and returns as list

    :parameters: 
        self -> service class object.
        params -> dict : params passed to the func of the service object.
        url -> str: where the request will be performed.
        targeted_service -> str: the service key we are looking for in the response.
    :return: List of dictionaries that support attriubte-style access, which represent collection of Customers.
    :rtype: list
    '''
    total_pages = 0
    _, _, raw_response = self.http_client.get(
        url, params=params, **{'raw': True}) ## gets the raw data from fortnox
    meta_data = raw_response.get('MetaInformation')
    if meta_data:
        total_pages = meta_data.get('@TotalPages', 0) ## gets the total number of pages
    
    services = raw_response.get(targeted_service) ## gets the targeted service of 1st page
    
    if total_pages > 1:
        ## gets the targeted service from page 2 to last page and concat then in services
        for page in range(2, total_pages+1):
            params['page'] = page
            _, _, response = self.http_client.get(url, params=params)
            services = services + response
    return services
