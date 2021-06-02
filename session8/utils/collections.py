def filter_by(collection, key, value):
    return list( filter(lambda x: x[key] == value, collection) )


def unique_by_key(collection, key):
    #Definir los keys

    keys = []
    for item in collection:
        if not item[key] in keys:
            keys.append(item[key])
    
    return keys

    
    # map(lambda x: keys.append(x[key], collection))
    #item [ key ] in keys ? pass : keys.append(x[key])

