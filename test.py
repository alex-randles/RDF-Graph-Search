from SPARQLWrapper import SPARQLWrapper, JSON, XML, CSV
sparql = SPARQLWrapper("https://blazegraph.virtualtreasury.ie/blazegraph/namespace/b2022/sparql")
sparql.setQuery("""
    PREFIX crm: <http://erlangen-crm.org/current/>
    SELECT * WHERE {
           ?person a crm:E21_Person . 
    } 
    LIMIT 2
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
sparql_variables = results["head"]["vars"]
print(sparql_variables)
print(results["results"]["bindings"])
for result in results["results"]["bindings"]:
    for variable in sparql_variables:
        print(result.get(variable).get("value"))