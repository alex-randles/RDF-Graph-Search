# RDF-Graph-Searcher

The following repository includes a Python web application which can be used to execute and display the results of SPARQL queries executed on a specified endpoint.



### Installation Guide

### Requirements 
The `requirements.txt` file contains the two libraries which are required to run the application. 
[Flask] 
[SPARQLWrapper]

The requirements can be installed using the following command: `pip3 install -r requirements.txt` 
### Running the Application
The application can be started using the following command: `python main.py`


The interface of the application will run on localhost port 5000 by default [127.0.0.1:5000](http://127.0.0.1:5000)

### Changing the SPARQL Query
The SPARQL query executed by the application can be changed by editing the `sparql_query` variable on line 21 of `main.py`. 

The string `{search_term}` in the SPARQL query will be replaced by the search term entered interface.

### Sample Query 
The SPARQL query already included in `main.py` can be executed on the [Virtual Treasury Knowlege Graph](https://virtualtreasury.ie/knowledge-graph). The query will return people with name entered into the interface. 

The sample query can be executed by accessing the interface, **selecting the VRTI endpoint from the dropdown on the right** and entering a name. 




Please contact alex.randles@adaptcentre.ie with any issues. 