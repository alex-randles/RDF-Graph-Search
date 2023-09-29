# RDF-Graph-Search

The following repository includes a Python web application which can be used to execute and display the results of SPARQL queries on endpoints.



### Installation Guide
The following sections cover the installation and running of the application. The application requires `python 3.10` or greater to run.
### Downloding Source Code 
The following command can be used to download this repository: `git clone https://github.com/alex-randles/RDF-Graph-Search.git`

Alternatively, you can download the a ZIP file containing the code here: [https://github.com/alex-randles/RDF-Graph-Search/archive/refs/heads/main.zip](https://github.com/alex-randles/RDF-Graph-Search/archive/refs/heads/main.zip)
### Requirements 
The `requirements.txt` file contains the two packages which are required to run the application. 
* [Flask](https://pythonbasics.org/what-is-flask-python/): Responsible for hosting the web application. 
* [SPARQLWrapper](https://rdflib.dev/sparqlwrapper/doc/1.8.5/main.html): Responsible for executing SPARQL queries on endpoints. 

The packages can be installed using the following command: `pip3 install -r requirements.txt` 
### Running the Application
The application can be started using the following command: `python3 main.py`

The interface of the application will run on localhost port 5000 by default [127.0.0.1:5000](http://127.0.0.1:5000).

The port can be configured on line 66 of `main.py` by changing the respective variable `app.run(debug=True, host="127.0.0.1", port=5000)`

### Changing the SPARQL Query
The SPARQL query executed by the application can be changed by editing the `sparql_query` variable on line 20 of `main.py`. 

The string `{query_parameter}` in the SPARQL query will be replaced by the query parameter entered into the interface.

### Sample Query 
The SPARQL query already included in `main.py` can be executed on the [Virtual Treasury Knowlege Graph](https://virtualtreasury.ie/knowledge-graph). The query will return people with the name entered into the interface. 

The sample query can be executed by accessing the interface, **selecting the VRTI endpoint from the dropdown on the right** and entering a name. The sample query will <u>**not return a result**</u> for any other endpoint available in the dropdown.
