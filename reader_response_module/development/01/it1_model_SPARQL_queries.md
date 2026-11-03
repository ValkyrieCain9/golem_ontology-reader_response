# Iteration 1 - Full Model - SPARQL Queries

## Query 1

### Identifier
SQ_1.1

### Query
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> <br />
PREFIX owl: <http://www.w3.org/2002/07/owl#> <br />
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> <br />
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> <br />
PREFIX crm: <http://erlangen-crm.org/240307/> <br />
PREFIX dcterms: <http://purl.org/dc/terms/> <br />
PREFIX dlp_lite: <http://www.ontologydesignpatterns.org/ont/dlp/DOLCE-Lite.owl#> <br />
PREFIX r: <https://w3id.org/golem/ontology/response#> <br />
PREFIX rd: <https://w3id.org/golem/ontology/response/data#> <br />

SELECT ?comment <br />
WHERE { <br />
?post rdf:type r:Post ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:has_comment ?comment . <br />
} <br />

### Based on
CQ_1.1

## Query 2

### Identifier
SQ_1.2

### Query
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> <br />
PREFIX owl: <http://www.w3.org/2002/07/owl#> <br />
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> <br />
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> <br />
PREFIX crm: <http://erlangen-crm.org/240307/> <br />
PREFIX dcterms: <http://purl.org/dc/terms/> <br />
PREFIX dlp_lite: <http://www.ontologydesignpatterns.org/ont/dlp/DOLCE-Lite.owl#> <br />
PREFIX r: <https://w3id.org/golem/ontology/response#> <br />
PREFIX rd: <https://w3id.org/golem/ontology/response/data#> <br />

SELECT ?thread ?parentComment <br />
WHERE { <br />
?parentComment rdf:type r:Comment ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:has_reply ?comment ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;dlp_lite:part_of ?thread . <br />
} <br />

### Based on
CQ_1.2

## Query 3

### Identifier
SQ_1.3

### Query
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> <br />
PREFIX owl: <http://www.w3.org/2002/07/owl#> <br />
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> <br />
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> <br />
PREFIX crm: <http://erlangen-crm.org/240307/> <br />
PREFIX dcterms: <http://purl.org/dc/terms/> <br />
PREFIX dlp_lite: <http://www.ontologydesignpatterns.org/ont/dlp/DOLCE-Lite.owl#> <br />
PREFIX r: <https://w3id.org/golem/ontology/response#> <br />
PREFIX rd: <https://w3id.org/golem/ontology/response/data#> <br />

SELECT ?comment ?rating_system ?rating_value <br />
WHERE { <br />
?comment rdf:type r:Comment ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;crm:P140i_was_attributed_by ?rating . <br />
?rating crm:P177_assigned_property_of_type ?rating_system ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;crm:P141_assigned ?value . <br />
?value crm:P90_hasValue ?rating_value . <br />
} <br />

### Based on
CQ_1.3
