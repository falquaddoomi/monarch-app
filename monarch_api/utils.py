import requests, collections

solr_url = "http://localhost:8983/solr"
association_url = "http://localhost:8983/solr/association"


def strip_json(doc: dict, *fields_to_remove: str):
    for field in fields_to_remove:
        try:
            del doc[field]
        except:
            pass
    return doc

def build_association_query(args: dict) -> str:
    query = "?"
    query_params = ['q', 'offset', 'limit']
    filter_params = ['subject', 'object', 'predicate', 'entity', 'category', 'between']
    for i in query_params:
        if args[i] == None:
            pass
        elif i in query_params:
            query += f'{i}={args[i]}&'
    query += "fq="
    for i in filter_params:
        if args[i] == None:
            pass
        elif i == 'entity':
            query += f'subject:"{i}" OR object:"{i}"&'
        elif i == 'between':
            between = args[i].split(",")
            query += f'(subject:"{between[0]}" AND object:"{between[1]}") OR (subject:"{between[1]}" AND object:"{between[0]}")&'
        else:
            query += f'{i}:"{args[i]}"&'
    return query

def get_associations(
    q: str = "*:*",
    offset: int = 0,
    limit: int = 20,
    category: str = None,
    predicate: str = None,
    subject: str = None,
    object: str = None,
    entity: str = None, # return nodes where entity is subject or object
    between: str = None # strip by comma and check associations in both directions. example: "MONDO:000747,MONDO:000420"
    ):

    query = build_association_query(locals())
    
    association_url = f"{solr_url}/association/query"
    url = association_url+query
    r = requests.get(url)
    results = r.json()['response']['docs']
    return results


def get_filtered_facet(entity_id, filter_field, facet_field):
    response = requests.get(f"{association_url}/select?q=*:*&limit=0&facet=true&facet.field={facet_field}&fq={filter_field}:\"{entity_id}\"")
    facet_fields = response.json()["facet_counts"]["facet_fields"][facet_field]
    
    return dict(zip(facet_fields[::2], facet_fields[1::2]))


def get_entity_association_counts(entity_id):
    object_categories = get_filtered_facet(entity_id, filter_field="subject", facet_field="object_category")
    subject_categories = get_filtered_facet(entity_id, filter_field="object", facet_field="subject_category")
    categories = collections.Counter(object_categories) + collections.Counter(subject_categories)
    return categories