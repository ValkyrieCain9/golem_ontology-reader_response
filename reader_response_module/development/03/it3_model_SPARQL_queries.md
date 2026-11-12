# Iteration 3 - Full Model - SPARQL Queries

## Query 1

### Identifier
SQ_3.1

### Query
PREFIX crm: <http://erlangen-crm.org/240307/> <br />
PREFIX crmdig: <http://www.cidoc-crm.org/extensions/crmdig/> <br />
PREFIX golem: <https://w3id.org/golem/ontology#> <br />
PREFIX lrmoo: <https://cidoc-crm.org/extensions/lrmoo/owl/> <br />
PREFIX owl: <http://www.w3.org/2002/07/owl#> <br />
PREFIX r: <https://w3id.org/golem/ontology/response#> <br />
PREFIX rd: <https://w3id.org/golem/ontology/response/data#> <br />
PREFIX schema1: <http://schema.org/> <br />
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> <br />
SELECT ?discourse_act ?discourse_type ?subject ?subj_title <br />
WHERE { <br />
?discourse_act rdf:type r:Discourse_Act; <br />
&nbsp;&nbsp;&nbsp;&nbsp;crm:P2_has_type ?discourse_type ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;crm:P129_is_about ?subject . <br />
?subject schema1:title ?subj_title . <br />
} <br />

### Based on
CQ_3.1

## Query 2

### Identifier
SQ_3.2

### Query
PREFIX crm: <http://erlangen-crm.org/240307/> <br />
PREFIX crmdig: <http://www.cidoc-crm.org/extensions/crmdig/> <br />
PREFIX golem: <https://w3id.org/golem/ontology#> <br />
PREFIX lrmoo: <https://cidoc-crm.org/extensions/lrmoo/owl/> <br />
PREFIX owl: <http://www.w3.org/2002/07/owl#> <br />
PREFIX r: <https://w3id.org/golem/ontology/response#> <br />
PREFIX rd: <https://w3id.org/golem/ontology/response/data#> <br />
PREFIX schema1: <http://schema.org/> <br />
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> <br />
SELECT ?clause ?type ?topic ?sentiment ?feature ?golem_class <br />
WHERE { <br />
?clause rdf:type r:Discourse_Act ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;crm:P148i_is_component_of rd:GoodReadsReview ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;crm:P2_has_type ?type . <br />
OPTIONAL {?clause r:has_topic ?topic.} <br />
OPTIONAL {?clause r:has_sentiment ?sentiment.} <br />
OPTIONAL { <br />
?clause crm:P67_refers_to ?feature . <br />
?topic rdf:type ?golem_class . <br />
} <br />
} <br />

### Based on
CQ_3.2

## Query 3

### Identifier
SQ_3.3

### Query
PREFIX crm: <http://erlangen-crm.org/240307/> <br />
PREFIX crmdig: <http://www.cidoc-crm.org/extensions/crmdig/> <br />
PREFIX golem: <https://w3id.org/golem/ontology#> <br />
PREFIX lrmoo: <https://cidoc-crm.org/extensions/lrmoo/owl/> <br />
PREFIX owl: <http://www.w3.org/2002/07/owl#> <br />
PREFIX r: <https://w3id.org/golem/ontology/response#> <br />
PREFIX rd: <https://w3id.org/golem/ontology/response/data#> <br />
PREFIX schema1: <http://schema.org/> <br />
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> <br />
SELECT ?actor ?role ?discourse_act ?discourse_type ?parent_discourse <br />
WHERE { <br />
?discourse_act rdf:type r:Discourse_Act ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;crm:P129_is_about rd:ao3Fanfic ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;crm:P2_has_type ?discourse_type ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:encoded_by ?dig_obj ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:responds_to ?parent_discourse . <br />
?action rdf:type crmdig:D7_Digital_Machine_Event ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;crmdig:L11_had_output ?dig_obj ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;crm:P14_carried_out_by ?actor . <br />
?actor r:has_user_role ?role . <br />
} <br />

### Based on
CQ_3.3

## Query 4

### Identifier
SQ_3.4

### Query
PREFIX crm: <http://erlangen-crm.org/240307/> <br />
PREFIX crmdig: <http://www.cidoc-crm.org/extensions/crmdig/> <br />
PREFIX golem: <https://w3id.org/golem/ontology#> <br />
PREFIX lrmoo: <https://cidoc-crm.org/extensions/lrmoo/owl/> <br />
PREFIX owl: <http://www.w3.org/2002/07/owl#> <br />
PREFIX r: <https://w3id.org/golem/ontology/response#> <br />
PREFIX rd: <https://w3id.org/golem/ontology/response/data#> <br />
PREFIX schema1: <http://schema.org/> <br />
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> <br />
SELECT ?comment ?comment_type ?parent_comment ?thread ?thread_type <br />
WHERE { <br />
?comment rdf:type r:Discourse_Act ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;crm:P129_is_about rd:anime ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;crm:P2_has_type ?comment_type ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:responds_to ?parent_comment ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:encoded_by ?dig_obj . <br />
?thread rdf:type r:Thread ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;r:has_comment ?dig_obj ; <br />
&nbsp;&nbsp;&nbsp;&nbsp;crm:P2_has_type ?thread_type . <br />
} <br />

### Based on
CQ_3.4
