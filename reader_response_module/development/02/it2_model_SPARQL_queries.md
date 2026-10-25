# Iteration 2 - Full Model - SPARQL Queries

## Query 1

### Identifier
SQ_2.1

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> <br />
PREFIX owl: <http://www.w3.org/2002/07/owl#> <br />
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> <br />
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> <br />
PREFIX crm: <http://erlangen-crm.org/240307/> <br />
PREFIX crmdig: <http://www.cidoc-crm.org/extensions/crmdig/> <br />
PREFIX r: <https://w3id.org/golem/ontology/response#> <br />
PREFIX rd: <https://w3id.org/golem/ontology/response/data#> <br />
PREFIX schema1: <http://schema.org/> <br />

SELECT ?webpage ?page_url ?website ?website_domain <br />
WHERE { <br />
?website rdf:type crmdig:D1_Digital_Object ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;crm:P2_has_type schema1:WebSite ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:has_webpage ?webpage ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;schema1:url ?website_domain . <br />
?webpage schema1:url ?page_url . <br />
} <br />

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
PREFIX crm: <http://erlangen-crm.org/240307/> <br />
PREFIX crmdig: <http://www.cidoc-crm.org/extensions/crmdig/> <br />
PREFIX r: <https://w3id.org/golem/ontology/response#> <br />
PREFIX rd: <https://w3id.org/golem/ontology/response/data#> <br />
PREFIX schema1: <http://schema.org/> <br />

SELECT ?website ?obj ?obj_type ?media ?media_type <br />
WHERE { <br />
?website rdf:type crmdig:D1_Digital_Object ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;crm:P2_has_type schema1:WebSite ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:has_webpage ?webpage . <br />
?obj r:encoded_by ?webpage ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;crm:P2_has_type ?obj_type ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;schema1:associatedMedia ?media . <br />
?media crm:P2_has_type ?media_type . <br />
} <br />

### Based on
CQ_2.2

## Query 3

### Identifier
SQ_2.3

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> <br />
PREFIX owl: <http://www.w3.org/2002/07/owl#> <br />
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> <br />
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> <br />
PREFIX crm: <http://erlangen-crm.org/240307/> <br />
PREFIX crmdig: <http://www.cidoc-crm.org/extensions/crmdig/> <br />
PREFIX r: <https://w3id.org/golem/ontology/response#> <br />
PREFIX rd: <https://w3id.org/golem/ontology/response/data#> <br />
PREFIX schema1: <http://schema.org/> <br />

SELECT ?obj ?obj_type ?media ?media_type ?result_of_action ?user <br />
WHERE { <br />
?obj rdf:type crmdig:D1_Digital_Object ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:encoded_by ?webpage ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;crm:P2_has_type ?obj_type ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;schema1:associatedMedia ?media . <br />
?media crm:P2_has_type ?media_type . <br />
?action crmdig:L11_had_output ?obj ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;crm:P2_has_type ?result_of_action ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;crm:P14_carried_out_by ?user . <br />
} <br />

### Based on
CQ_2.3
