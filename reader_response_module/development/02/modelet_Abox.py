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

# for entities not in csv
index = 1  

# type individuals

## digital object types
SITE = RESPONSE_ONT.site
POST = RESPONSE_ONT.post
COMMENT = RESPONSE_ONT.comment
PROFILE_ACC = RESPONSE_ONT.profileAccount

## translation action types
COMMENTING = RESPONSE_ONT.commenting
POSTING = RESPONSE_ONT.posting

# read the csv
# change path to new data modelet
with open("reader_response_module/development/02/data_modelet.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:

        #digital objects
        comment_uri = RESPONSE_DATA[row["comment"].strip()]
        g.add((comment_uri, RDF.type, RESPONSE_ONT.Digital_Object))
        g.add((comment_uri, RDF.type, RESPONSE_ONT.Bearer))
        g.add((comment_uri, RESPONSE_ONT.has_type, COMMENT))

        post_uri = RESPONSE_DATA[row["post"].strip()]
        g.add((post_uri, RDF.type, RESPONSE_ONT.Digital_Object))
        g.add((post_uri, RDF.type, RESPONSE_ONT.Bearer))
        g.add((post_uri, RESPONSE_ONT.has_type, POST))
        #
        g.add((post_uri, DCTERMS.title, Literal(row["post_title"].strip())))

        site_uri = RESPONSE_DATA[row["site"].strip()]
        g.add((site_uri, RDF.type, RESPONSE_ONT.Digital_Object))
        g.add((site_uri, RDF.type, RESPONSE_ONT.Bearer))
        g.add((site_uri, RESPONSE_ONT.has_type, SITE))
        #
        g.add((site_uri, SDO.name, Literal(row["site"].strip())))
        

        #users
        post_creator_uri = RESPONSE_DATA[row["post_creator_id"].strip()]
        g.add((post_creator_uri, RDF.type, RESPONSE_ONT.User))
        #
        p_creator_acc_uri = RESPONSE_DATA[row["post_creator_acc"].strip()]
        g.add((p_creator_acc_uri, RDF.type, RESPONSE_ONT.Digital_Object))
        g.add((p_creator_acc_uri, RESPONSE_ONT.has_type, PROFILE_ACC))
        g.add((post_creator_uri, RESPONSE_ONT.has_account, p_creator_acc_uri))
        ##
        g.add((p_creator_acc_uri, SDO.name, Literal(row["post_creator_acc"].strip())))
        
        comment_creator_uri = RESPONSE_DATA[row["comment_creator_id"].strip()]
        g.add((comment_creator_uri, RDF.type, RESPONSE_ONT.User))
        #
        c_creator_acc_uri = RESPONSE_DATA[row["comment_creator_acc"].strip()]
        g.add((c_creator_acc_uri, RDF.type, RESPONSE_ONT.Digital_Object))
        g.add((c_creator_acc_uri, RESPONSE_ONT.has_type, PROFILE_ACC))
        g.add((comment_creator_uri, RESPONSE_ONT.has_account, c_creator_acc_uri))
        ##
        g.add((c_creator_acc_uri, SDO.name, Literal(row["comment_creator_acc"].strip())))

        #expressions
        c_exp_uri = RESPONSE_DATA[f"comment_expression_{index}"]
        g.add((c_exp_uri, RDF.type, RESPONSE_ONT.Expression))
        g.add((c_exp_uri, RESPONSE_ONT.created_by, comment_creator_uri))
        #
        g.add((c_exp_uri, RESPONSE_ONT.has_value, Literal(row["comment_expression"].strip())))

        p_exp_uri = RESPONSE_DATA[f"post_expression_{index}"]
        g.add((p_exp_uri, RDF.type, RESPONSE_ONT.Expression))
        g.add((p_exp_uri, RESPONSE_ONT.created_by, post_creator_uri))    
        #
        g.add((p_exp_uri, RESPONSE_ONT.has_value, Literal(row["post_expression"].strip())))    

        #translation actions
        posting_action_uri = RESPONSE_DATA[f"posting_action_{index}"]
        g.add((posting_action_uri, RDF.type, RESPONSE_ONT.Translation_Action))
        g.add((posting_action_uri, RESPONSE_ONT.has_type, POSTING))
        g.add((posting_action_uri, RESPONSE_ONT.results_in, post_uri))
        g.add((posting_action_uri, RESPONSE_ONT.performed_by, post_creator_uri))
        g.add((p_exp_uri, RESPONSE_ONT.translated_by, posting_action_uri))

        commenting_action_uri = RESPONSE_DATA[f"commenting_action_{index}"]
        g.add((commenting_action_uri, RDF.type, RESPONSE_ONT.Translation_Action))
        g.add((commenting_action_uri, RESPONSE_ONT.has_type, COMMENTING))
        g.add((commenting_action_uri, RESPONSE_ONT.results_in, comment_uri))
        g.add((commenting_action_uri, RESPONSE_ONT.performed_by, comment_creator_uri))
        g.add((c_exp_uri, RESPONSE_ONT.translated_by, commenting_action_uri))                

        #bearers of immaterial objects
        g.add((comment_uri, RESPONSE_ONT.has_bearer, site_uri))
        g.add((post_uri, RESPONSE_ONT.has_bearer, site_uri))
        g.add((p_creator_acc_uri, RESPONSE_ONT.has_bearer, site_uri))
        g.add((c_creator_acc_uri, RESPONSE_ONT.has_bearer, site_uri))
        g.add((c_exp_uri, RESPONSE_ONT.has_bearer, comment_uri))
        g.add((p_exp_uri, RESPONSE_ONT.has_bearer, post_uri))

        index += 1

# save
g.serialize(destination="reader_response_module/development/02/modelet_ABox.ttl", format="turtle")
print("RDF file successfully saved as 'modelet_ABox.ttl'")