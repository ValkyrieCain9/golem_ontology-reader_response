import csv
from rdflib import Graph, Namespace, Literal, RDF, URIRef, RDFS, OWL, DCTERMS, SDO
from rdflib.namespace import XSD

#rdflib namespace SDO = schema.org

RESPONSE_ONT = Namespace("https://w3id.org/golem/ontology/response#")
RESPONSE_DATA = Namespace("https://w3id.org/golem/ontology/response/data#")

# Graph
g = Graph()
# g.parse("reader_response_module/development/01/modelet_TBox.ttl", format="turtle")

g.bind("r", RESPONSE_ONT)
g.bind("rd", RESPONSE_DATA)

g.add((URIRef("https://w3id.org/golem/ontology/response/data#"), RDF.type, OWL.Ontology))
g.add((
    URIRef("https://w3id.org/golem/ontology/response/data#"),
    OWL.imports,
    # change uri to current ttl modelet
    URIRef("file:///Users/regina/Documents/UNIBO/Thesis/GOLEM/golem_ontology-reader_response/reader_response_module/development/02/modelet_TBox.ttl")
))

# read the csv
# change path to new data modelet
with open("reader_response_module/development/02/data_modelet.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:

        #webpage
        webpage_uri = RESPONSE_DATA[row["object_webpage_id"].strip()]
        g.add((webpage_uri, RDF.type, RESPONSE_ONT.Digital_Object))
        g.add((webpage_uri, RESPONSE_ONT.has_bitstring_type, RESPONSE_ONT.webpage))
        g.add((webpage_uri, SDO.url, URIRef(row["object_webpage_path"])))
        
        #website
        website_uri = RESPONSE_DATA[row["website_id"].strip()]
        g.add((website_uri, RDF.type, RESPONSE_ONT.Website))
        g.add((website_uri, SDO.url, URIRef(row["website_domain"])))
        g.add((website_uri, RESPONSE_ONT.has_webpage, webpage_uri))

        #user
        user_uri = RESPONSE_DATA[row["user_id"].strip()]
        g.add((user_uri, RDF.type, RESPONSE_ONT.User))

        #posting action
        action_uri = RESPONSE_DATA[f'{row["object_id"].strip()}_Action']
        g.add((action_uri, RDF.type, RESPONSE_ONT.Translation_Action))
        g.add((action_uri, RESPONSE_ONT.has_translation_action_type, RESPONSE_ONT[row["action_type"].strip()]))
        g.add((action_uri, RESPONSE_ONT.performed_by, user_uri))
        if row["action_type"] == "posting":
            g.add((webpage_uri, RESPONSE_ONT.result_of, action_uri))

        #object
        obj_uri = RESPONSE_DATA[row["object_id"].strip()]
        if row["object_type"] != "Textual_Expression":
            g.add((obj_uri, RDF.type, RESPONSE_ONT.Digital_Object))
            g.add((obj_uri, RESPONSE_ONT.has_type, RESPONSE_ONT[row["object_type"].strip()]))
        else:
            g.add((obj_uri, RDF.type, RESPONSE_ONT.Textual_Expression))
            g.add((obj_uri, RESPONSE_ONT.has_value, Literal([row["object_content"].strip()])))
        g.add((obj_uri, RESPONSE_ONT.created_by, user_uri))
        g.add((obj_uri, RESPONSE_ONT.has_bearer, webpage_uri))
        g.add((obj_uri, RESPONSE_ONT.translated_by, action_uri))

# save
g.serialize(destination="reader_response_module/development/02/modelet_ABox.ttl", format="turtle")
print("RDF file successfully saved as 'modelet_ABox.ttl'")