# Modelet - SPARQL Queries

## Query 1

### Identifier
sq_2.1

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> <br />
PREFIX owl: <http://www.w3.org/2002/07/owl#> <br />
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> <br />
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> <br />
PREFIX r: <https://w3id.org/golem/ontology/response#> <br />
PREFIX rd: <https://w3id.org/golem/ontology/response/data#> <br />
PREFIX schema: <https://schema.org/> <br />
SELECT ?webpage ?website <br />
WHERE { <br />
?webpage rdf:type r:Digital_Object ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:has_bitstring_type r:webpage . <br />
?website rdf:type r:Website; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:has_webpage ?webpage . <br />
}

### Based on
CQ_2.1

## Query 2

### Identifier
sq_2.2

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

### Based on
CQ_2.2

## Query 3

### Identifier
sq_2.3

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> <br />
PREFIX owl: <http://www.w3.org/2002/07/owl#> <br />
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> <br />
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> <br />
PREFIX r: <https://w3id.org/golem/ontology/response#> <br />
PREFIX rd: <https://w3id.org/golem/ontology/response/data#> <br />
SELECT ?obj ?obj_type ?translation_action ?user <br />
WHERE { <br />
?webpage rdf:type r:Digital_Object; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:has_bitstring_type r:webpage . <br />
?obj r:has_bearer ?webpage ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;rdf:type ?obj_type ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:translated_by ?action . <br />
?action r:has_translation_action_type ?translation_action ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:performed_by ?user . <br />
}

### Based on
CQ_2.3
