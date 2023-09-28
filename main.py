from SPARQLWrapper import SPARQLWrapper, JSON
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = "x633UE2xYRC"

@app.route('/', methods=["GET"])
def index():
    if request.method == "GET":
        search_graph_uri = "https://blazegraph.virtualtreasury.ie"
        return render_template("index.html",
                               search_graph_uri=search_graph_uri
                               )


@app.route('/search-graph', methods=["GET", "POST"])
def search_graph():
    search_term = request.form.get("search_term")
    graph_uri = request.form.get("graph_uri")
    print(search_term, graph_uri)
    # VRTI Query
    sparql_query = """
    PREFIX crm: <http://erlangen-crm.org/current/>
    PREFIX vrti: <http://ont.virtualtreasury.ie/ontology#>
    SELECT DISTINCT ?person ?occupation ?gender
    WHERE {
      ?person ?predicate ?object; 
          crm:P1_is_identified_by ?name;
           crm:P2_has_type  ?gender;
          a crm:E21_Person .
      ?occupation crm:P107_has_current_or_former_member ?person ;
                  rdfs:label ?occupationName   .
      ?name rdfs:label ?nameLabel  ;
            a   crm:E41_Appellation  . 
      FILTER CONTAINS(LCASE(?nameLabel),'{search_term}')     
     }
    LIMIT 100
    """
    # DBpedia Query
    # sparql_query = f"""
    #     PREFIX dbo: <http://dbpedia.org/ontology/>
    #     SELECT ?athlete ?place
    #     WHERE
    #     {{
    #       ?athlete  rdfs:label      ?label ;
    #                 dbo:birthPlace  ?place .
    #       ?place    a               dbo:City ;
    #                 rdfs:label      ?cityName .
    #                 FILTER (STR(?cityName) = '{search_term}')
    #     }}
    #     LIMIT 100
    # """
    # Wikidata Query
    # sparql_query = f"""
    # PREFIX wd: <http://www.wikidata.org/entity/>
    # PREFIX wdt: <http://www.wikidata.org/prop/direct/>
    # SELECT DISTINCT ?item ?itemLabel ?occupationLabel
    # WHERE
    # {{
    #       ?item wdt:P31 wd:Q5;
    #           wdt:P19/wdt:P131* wd:Q60;
    #           wdt:P27 wd:Q30;
    #           wdt:P106 ?occupation;
    #           rdfs:label ?itemLabel .
    #      ?occupation wdt:P3321 ?occupationLabel  .
    #      FILTER(LANG(?itemLabel) = "en" && LANG(?occupationLabel) = "en" && STR(?occupationLabel) = "{search_term}")
    # }}
    # LIMIT 10
    # """
    # Add the search term to the SPARQL query
    sparql_query = sparql_query.replace("{search_term}", search_term)
    table_rows = {}
    try:
        sparql = SPARQLWrapper(graph_uri)
        sparql.setQuery(sparql_query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        row_count = 0
        sparql_variables = sorted(results["head"]["vars"])
        print(f"The following variables are returned by the SPARQL query: {sparql_variables}")
        for result in results["results"]["bindings"]:
            new_row = {}
            for variable in sparql_variables:
                if result.get(variable):
                    current_value = result.get(variable).get("value")
                    new_row[variable] = current_value
            table_rows[row_count] = new_row
            row_count += 1
        print(f"The results of the query: {table_rows}")
        print(f"The SPARQL query executed:\n {sparql_query}")
        return table_rows
    except Exception as e:
        exception_message = f"Exception: {e}"
        print(exception_message)
        return exception_message



if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)
