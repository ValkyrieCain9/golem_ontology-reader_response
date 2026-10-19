# Modelet - SPARQL Queries

## Query 1

### Identifier
SQ_2.1

-

### Based on
CQ_2.1

## Query 2

### Identifier
SQ_2.2

### Query
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> <br />
PREFIX owl: <http://www.w3.org/2002/07/owl#> <br />
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> <br />
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> <br />
PREFIX r: <https://w3id.org/golem/ontology/response#> <br />
PREFIX rd: <https://w3id.org/golem/ontology/response/data#> <br />
PREFIX schema: <https://schema.org/> <br />
SELECT ?website ?digObj ?type <br />
WHERE { <br />
?website rdf:type r:Website ;<br />
&nbsp;&nbsp;&nbsp;&nbsp;r:has_webpage ?webpage .<br />
?digObj rdf:type r:Digital_Object ;<br />
&nbsp;&nbsp;&nbsp;&nbsp;r:has_bearer ?webpage ;<br />
&nbsp;&nbsp;&nbsp;&nbsp;r:has_type ?type .<br />
}

## Query 3

### Identifier
SQ_2.3

-

### Based on
CQ_2.3

### Based on
CQ_2.2
