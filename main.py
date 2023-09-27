from SPARQLWrapper import SPARQLWrapper, JSON
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        search_graph_uri = "https://blazegraph.virtualtreasury.ie"
        return render_template("index.html",
                               search_graph_uri=search_graph_uri
                               )
    else:
        print("data posted")
        print(request.form)
        return "dhdhdh"


@app.route('/search-graph', methods=["GET", "POST"])
def search_graph():
    search_term = request.form.get("search_term")
    graph_uri = request.form.get("graph_uri")
    print(search_term, graph_uri)
    sparql_query = f"""
    PREFIX crm: <http://erlangen-crm.org/current/>
    SELECT DISTINCT ?subject ?nameLabel
    WHERE {{
      ?subject ?predicate ?object; 
          crm:P1_is_identified_by ?name;
          a crm:E21_Person .
      ?name rdfs:label ?nameLabel . 
      FILTER CONTAINS(LCASE(?nameLabel),'{search_term}')     
     }}
    LIMIT 1000
    """
    table_rows = {}
    try:
        sparql = SPARQLWrapper(graph_uri)
        sparql.setQuery(sparql_query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        row_count = 0
        sparql_variables = sorted(results["head"]["vars"])
        print(sparql_variables)
        for result in results["results"]["bindings"]:
            new_row = {}
            for variable in sparql_variables:
                current_value = result.get(variable).get("value")
                new_row[variable] = current_value
            table_rows[row_count] = new_row
            row_count += 1
        print(table_rows)
        return table_rows
    except Exception as e:
        print(e)
        return table_rows


if __name__ == '__main__':
    app.run(debug=True)
