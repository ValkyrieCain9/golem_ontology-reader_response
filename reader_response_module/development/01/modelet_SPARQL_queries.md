# Modelet - SPARQL Queries

## Query 1

### Identifier
sq_1.1

### Query
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> <br />
PREFIX owl: <http://www.w3.org/2002/07/owl#> <br />
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> <br />
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> <br />
PREFIX dcterms: <http://purl.org/dc/terms/> <br />
PREFIX r: <https://w3id.org/golem/ontology/response#> <br />
PREFIX rd: <https://w3id.org/golem/ontology/response/data#> <br />
SELECT ?comment <br />
WHERE { <br />
?site r:hasPost ?post . <br />
?post r:hasComment ?comment . <br />
} <br />

### Based on
CQ_1.1

## Query 2

### Identifier
sq_1.2

### Query
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> <br />
PREFIX owl: <http://www.w3.org/2002/07/owl#> <br />
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> <br />
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> <br />
PREFIX dcterms: <http://purl.org/dc/terms/> <br />
PREFIX r: <https://w3id.org/golem/ontology/response#> <br />
PREFIX rd: <https://w3id.org/golem/ontology/response/data#> <br />
SELECT ?thread ?parentComment <br />
WHERE { <br />
?parentComment rdf:type r:Comment ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:hasReply ?comment ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:partOfThread ?thread . <br />
} <br />

### Based on
CQ_1.2

## Query 3

### Identifier
sq_1.3

### Query
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> <br />
PREFIX owl: <http://www.w3.org/2002/07/owl#> <br />
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> <br />
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> <br />
PREFIX dcterms: <http://purl.org/dc/terms/> <br />
PREFIX r: <https://w3id.org/golem/ontology/response#> <br />
PREFIX rd: <https://w3id.org/golem/ontology/response/data#> <br />
SELECT ?comment ?rating_system ?rating_value <br />
WHERE { <br />
?comment rdf:type r:Comment ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:hasRating ?rating . <br />
?rating r:hasRatingSystem ?rating_system ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:hasRatingValue ?rating_value . <br />
} <br />

### Based on
CQ_1.3
