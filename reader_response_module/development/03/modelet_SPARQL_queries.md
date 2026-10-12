# Modelet - SPARQL Queries

## Query 1

### Identifier
SQ_3.1

### Query
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> <br />
PREFIX owl: <http://www.w3.org/2002/07/owl#> <br />
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> <br />
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> <br />
PREFIX r: <https://w3id.org/golem/ontology/response#> <br />
PREFIX rd: <https://w3id.org/golem/ontology/response/data#> <br />
PREFIX dcterms: <http://purl.org/dc/terms/> <br />
SELECT ?review ?type ?subject <br />
WHERE { <br />
?review rdf:type r:Discourse_Act ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:has_type ?type ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:has_subject ?book . <br />

?book rdf:type r:Expression ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;dcterms:title ?subject . <br />
} <br />

### Based on
CQ_3.1

## Query 2

### Identifier
SQ_3.2

### Query
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> <br />
PREFIX owl: <http://www.w3.org/2002/07/owl#> <br />
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> <br />
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> <br />
PREFIX r: <https://w3id.org/golem/ontology/response#> <br />
PREFIX rd: <https://w3id.org/golem/ontology/response/data#> <br />
PREFIX dcterms: <http://purl.org/dc/terms/> <br />
SELECT ?clause ?type ?theme ?sentiment ?value <br />
WHERE { <br />
?clause rdf:type r:Discourse_Act ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:part_of rd:GoodReadsReview ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:has_value ?value ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:has_type ?type . <br />
OPTIONAL {?clause r:has_theme ?theme.} <br />
OPTIONAL{?clause r:has_sentiment ?sentiment.} <br />
}

### Based on
CQ_3.2

## Query 3

### Identifier
SQ_3.3

### Query
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> <br />
PREFIX owl: <http://www.w3.org/2002/07/owl#> <br />
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> <br />
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> <br />
PREFIX r: <https://w3id.org/golem/ontology/response#> <br />
PREFIX rd: <https://w3id.org/golem/ontology/response/data#> <br />
PREFIX dcterms: <http://purl.org/dc/terms/> <br />
SELECT ?actor ?role ?comment ?responding_to ?discourse_act <br />
WHERE { <br />
?actor rdf:type r:Actor ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:has_role ?role ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:created ?comment . <br />
?comment rdf:type r:Discourse_Act ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:has_type ?discourse_act ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:responds_to ?responding_to . <br />
} <br />

### Based on
CQ_3.3

## Query 4

### Identifier
SQ_3.4

### Query
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> <br />
PREFIX owl: <http://www.w3.org/2002/07/owl#> <br />
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> <br />
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> <br />
PREFIX r: <https://w3id.org/golem/ontology/response#> <br />
PREFIX rd: <https://w3id.org/golem/ontology/response/data#> <br />
PREFIX dcterms: <http://purl.org/dc/terms/> <br />
SELECT ?comment ?type ?responding_to ?thread ?thread_type <br />
WHERE { <br />
?comment rdf:type r:Discourse_Act; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:has_type ?type ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:responds_to ?responding_to ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:part_of ?thread . <br />
?thread rdf:type r:Thread ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:has_threadType ?thread_type . <br />
} <br />

### Based on
CQ_3.4
