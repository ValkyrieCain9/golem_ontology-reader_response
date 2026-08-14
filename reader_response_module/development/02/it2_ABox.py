import csv
from rdflib import Graph, Namespace, Literal, RDF, URIRef, RDFS, OWL, DCTERMS, SDO
from rdflib.namespace import XSD

RESPONSE_ONT = Namespace("https://w3id.org/golem/ontology/response#")
RESPONSE_DATA = Namespace("https://w3id.org/golem/ontology/response/data#")
CRM = Namespace("http://erlangen-crm.org/240307/")
CRM_DIG = Namespace("http://www.cidoc-crm.org/extensions/crmdig/")
LRMOO = Namespace("https://cidoc-crm.org/extensions/lrmoo/owl/")
GOLEM = Namespace("https://w3id.org/golem/ontology#")

# Graph
g = Graph()
# g.parse("reader_response_module/development/01/modelet_TBox.ttl", format="turtle")

g.bind("r", RESPONSE_ONT)
g.bind("rd", RESPONSE_DATA)
g.bind("crm", CRM)
g.bind("crmdig", CRM_DIG)
g.bind("lrmoo", LRMOO)
g.bind("golem", GOLEM)

g.add((URIRef("https://w3id.org/golem/ontology/response/data#"), RDF.type, OWL.Ontology))
g.add((
    URIRef("https://w3id.org/golem/ontology/response/data#"),
    OWL.imports,
    URIRef("file:///Users/regina/Documents/UNIBO/Thesis/GOLEM/golem_ontology-reader_response/reader_response_module/development/02/it2_Tbox.ttl")
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
with open("reader_response_module/development/02/data_modelet.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:
        #digital objects
        comment_uri = RESPONSE_DATA[row["comment"].strip()]
        g.add((comment_uri, RDF.type, CRM_DIG.D1_Digital_Object))
        g.add((comment_uri, RDF.type, RESPONSE_ONT.Immaterial_Information_Carrier))
        g.add((comment_uri, CRM.P2_has_type, COMMENT))

        post_uri = RESPONSE_DATA[row["post"].strip()]
        g.add((post_uri, RDF.type, CRM_DIG.D1_Digital_Object))
        g.add((post_uri, RDF.type, RESPONSE_ONT.Immaterial_Information_Carrier))
        g.add((post_uri, CRM.P2_has_type, POST))
        #
        g.add((post_uri, DCTERMS.title, Literal(row["post_title"].strip())))

        site_uri = RESPONSE_DATA[row["site"].strip()]
        g.add((site_uri, RDF.type, CRM_DIG.D1_Digital_Object))
        g.add((site_uri, RDF.type, RESPONSE_ONT.Immaterial_Information_Carrier))
        g.add((site_uri, CRM.P2_has_type, SITE))
        #
        g.add((site_uri, SDO.name, Literal(row["site"].strip())))
        

        #users
        post_creator_uri = RESPONSE_DATA[row["post_creator_id"].strip()]
        g.add((post_creator_uri, RDF.type, RESPONSE_ONT.User))
        #
        p_creator_acc_uri = RESPONSE_DATA[row["post_creator_acc"].strip()]
        g.add((p_creator_acc_uri, RDF.type, CRM_DIG.D1_Digital_Object))
        g.add((p_creator_acc_uri, CRM.P2_has_type, PROFILE_ACC))
        g.add((p_creator_acc_uri, CRM.P105_right_held_by, post_creator_uri))
        ##
        g.add((p_creator_acc_uri, SDO.name, Literal(row["post_creator_acc"].strip())))
        
        comment_creator_uri = RESPONSE_DATA[row["comment_creator_id"].strip()]
        g.add((comment_creator_uri, RDF.type, RESPONSE_ONT.User))
        #
        c_creator_acc_uri = RESPONSE_DATA[row["comment_creator_acc"].strip()]
        g.add((c_creator_acc_uri, RDF.type, CRM_DIG.D1_Digital_Object))
        g.add((c_creator_acc_uri, CRM.P2_has_type, PROFILE_ACC))
        g.add((c_creator_acc_uri, CRM.P105_right_held_by, comment_creator_uri))
        ##
        g.add((c_creator_acc_uri, SDO.name, Literal(row["comment_creator_acc"].strip())))

        #expressions
        c_exp_uri = RESPONSE_DATA[f"comment_expression_{index}"]
        g.add((c_exp_uri, RDF.type, LRMOO.F2_Expression))
        g.add((c_exp_uri, CRM.P105_right_held_by, comment_creator_uri))
        #
        g.add((c_exp_uri, CRM.P190_has_symbolic_content, Literal(row["comment_expression"].strip())))

        p_exp_uri = RESPONSE_DATA[f"post_expression_{index}"]
        g.add((p_exp_uri, RDF.type, LRMOO.F2_Expression))
        g.add((p_exp_uri, CRM.P105_right_held_by, post_creator_uri))    
        #
        g.add((p_exp_uri, CRM.P190_has_symbolic_content, Literal(row["post_expression"].strip())))    

        #translation actions
        posting_action_uri = RESPONSE_DATA[f"posting_action_{index}"]
        g.add((posting_action_uri, RDF.type, CRM_DIG.D7_Digital_Machine_Event))
        g.add((posting_action_uri, CRM.P2_has_type, POSTING))
        g.add((posting_action_uri, CRM_DIG.L11_had_output, post_uri))
        g.add((posting_action_uri, CRM.P14_carried_out_by, post_creator_uri))
        g.add((posting_action_uri, CRM.P17_was_motivated_by, p_exp_uri))

        commenting_action_uri = RESPONSE_DATA[f"commenting_action_{index}"]
        g.add((commenting_action_uri, RDF.type, CRM_DIG.D7_Digital_Machine_Event))
        g.add((commenting_action_uri, CRM.P2_has_type, COMMENTING))
        g.add((commenting_action_uri, CRM_DIG.L11_had_output, comment_uri))
        g.add((commenting_action_uri, CRM.P14_carried_out_by, comment_creator_uri))
        g.add((commenting_action_uri, CRM.P17_was_motivated_by, c_exp_uri ))                

        #bearers of immaterial objects
        g.add((comment_uri, CRM.P130i_features_are_also_found_on
, site_uri))
        g.add((post_uri, CRM.P130i_features_are_also_found_on, site_uri))
        g.add((p_creator_acc_uri, CRM.P130i_features_are_also_found_on, site_uri))
        g.add((c_creator_acc_uri, CRM.P130i_features_are_also_found_on, site_uri))
        g.add((c_exp_uri, CRM.P130i_features_are_also_found_on, comment_uri))
        g.add((p_exp_uri, CRM.P130i_features_are_also_found_on, post_uri))

        index += 1

# save
g.serialize(destination="reader_response_module/development/02/it2_ABox.ttl", format="turtle")
print("RDF file successfully saved as 'it2_ABox.ttl'")