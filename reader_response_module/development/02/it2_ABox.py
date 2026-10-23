import csv
from rdflib import Graph, Namespace, Literal, RDF, URIRef, OWL
from rdflib.namespace import XSD

RESPONSE_ONT = Namespace("https://w3id.org/golem/ontology/response#")
RESPONSE_DATA = Namespace("https://w3id.org/golem/ontology/response/data#")
CRM = Namespace("http://erlangen-crm.org/240307/")
CRM_DIG = Namespace("http://www.cidoc-crm.org/extensions/crmdig/")
SCHEMA = Namespace("http://schema.org/")


# Graph
g = Graph()
# g.parse("reader_response_module/development/01/modelet_TBox.ttl", format="turtle")

g.bind("r", RESPONSE_ONT)
g.bind("rd", RESPONSE_DATA)
g.bind("crm", CRM)
g.bind("crmdig", CRM_DIG)
g.bind("schema", SCHEMA)


g.add((URIRef("https://w3id.org/golem/ontology/response/data#"), RDF.type, OWL.Ontology))
g.add((
    URIRef("https://w3id.org/golem/ontology/response/data#"),
    OWL.imports,
    URIRef("file:///Users/regina/Documents/UNIBO/Thesis/GOLEM/golem_ontology-reader_response/reader_response_module/development/02/it2_Tbox.ttl")
))

DIG_OBJ = CRM_DIG.D1_Digital_Object
DIG_EVENT = CRM_DIG.D7_Digital_Machine_Event

HAS_TYPE = CRM.P2_has_type

# read the csv
with open("reader_response_module/development/02/it2_data_model.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:

        #webpage
        webpage_uri = RESPONSE_DATA[row["object_webpage_id"].strip()]
        g.add((webpage_uri, RDF.type, DIG_OBJ))
        g.add((webpage_uri, HAS_TYPE, SCHEMA.WebPage))
        g.add((webpage_uri, SCHEMA.url, Literal(row["object_webpage_path"].strip(), datatype=XSD.anyURI)))
        
        #website
        website_uri = RESPONSE_DATA[row["website_id"].strip()]
        g.add((website_uri, RDF.type, DIG_OBJ))
        g.add((website_uri, HAS_TYPE, SCHEMA.WebSite))
        g.add((website_uri, SCHEMA.url, Literal(row["website_domain"].strip(), datatype=XSD.anyURI)))
        g.add((website_uri, RESPONSE_ONT.has_webpage, webpage_uri))

        #user
        user_uri = RESPONSE_DATA[row["user_id"].strip()]
        g.add((user_uri, RDF.type, RESPONSE_ONT.User))

        #media object
        media_obj_uri = RESPONSE_DATA[f'{row["object_id"].strip()}_Media']
        g.add((media_obj_uri, RDF.type, DIG_OBJ))
        g.add((media_obj_uri, HAS_TYPE, SCHEMA[row["media_object_type"].strip()]))
        if row["object_text"]:
            g.add((media_obj_uri, SCHEMA.text, Literal(row["object_text"].strip())))

        #object and action
        obj_uri = RESPONSE_DATA[row["object_id"].strip()]
        g.add((obj_uri, RDF.type, DIG_OBJ))
        g.add((obj_uri, RESPONSE_ONT.encoded_by, webpage_uri))
        g.add((obj_uri, SCHEMA.datePublished, Literal(row["date_published"].strip(), datatype=XSD.date)))
        if row["media_object_type"] != "SoftwareSourceCode" :
            g.add((obj_uri, SCHEMA.associatedMedia, media_obj_uri))
        else:
            g.add((obj_uri, CRM.P148_has_component, media_obj_uri))

        if row["view_count"]:
            g.add((obj_uri, RESPONSE_ONT.viewCount, Literal(int(row["view_count"].strip().replace(",", "")), datatype=XSD.integer)))

        if row["upvote_count"]:
            g.add((obj_uri, RESPONSE_ONT.upvoteCount, Literal(int(row["upvote_count"].strip().replace(",", "")), datatype=XSD.integer)))

        if row["like_count"]:
            g.add((obj_uri, RESPONSE_ONT.likeCount, Literal(int(row["like_count"].strip().replace(",", "")), datatype=XSD.integer)))

        action_uri = RESPONSE_DATA[f'{row["object_id"].strip()}_Action']
        g.add((action_uri, RDF.type, DIG_EVENT))
        g.add((action_uri, CRM.P14_carried_out_by, user_uri))
        g.add((user_uri, CRM.P14i_performed, action_uri))
        g.add((action_uri, CRM_DIG.L11_had_output, obj_uri))

        if row["action_type"] == "UserPosts":
            g.add((action_uri, HAS_TYPE, RESPONSE_ONT.UserPosts))
            g.add((obj_uri, HAS_TYPE, RESPONSE_ONT.Post))
        else:
            g.add((action_uri, HAS_TYPE, SCHEMA.UserComments))
            g.add((obj_uri, HAS_TYPE, SCHEMA.Comment))


# save
g.serialize(destination="reader_response_module/development/02/it2_ABox.ttl", format="turtle")
print("RDF file successfully saved as 'it2_ABox.ttl'")