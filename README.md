# python 2.7

    headers = {'Authorization': 'Basic XXX"}
    organizations = "XXX"
    
    apigee = ApigeeAPI(organizations,headers)
    
    result = apigee.search_consumerKey("XXXX")
    
    print apigee.get_developers()
    print apigee.get_developers_app(dev)
    print apigee.get_developers_app_details(dev,app)
    print apigee.list_developers_details_apps()
    print apigee.search_consumerKey(consumerKey)
