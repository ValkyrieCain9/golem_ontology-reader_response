import csv
from rdflib import Graph, Namespace, Literal, RDF, URIRef, OWL
from rdflib.namespace import XSD

RESPONSE_ONT = Namespace("https://w3id.org/golem/ontology/response#")
RESPONSE_DATA = Namespace("https://w3id.org/golem/ontology/response/data#")
CRM = Namespace("http://erlangen-crm.org/240307/")
CRM_DIG = Namespace("http://www.cidoc-crm.org/extensions/crmdig/")
SCHEMA = Namespace("http://schema.org/")
GOLEM = Namespace("https://w3id.org/golem/ontology#")
LRMOO = Namespace("https://cidoc-crm.org/extensions/lrmoo/owl/")


# Graph
g = Graph()
# g.parse("reader_response_module/development/01/modelet_TBox.ttl", format="turtle")

g.bind("r", RESPONSE_ONT)
g.bind("rd", RESPONSE_DATA)
g.bind("crm", CRM)
g.bind("crmdig", CRM_DIG)
g.bind("schema", SCHEMA)
g.bind("golem", GOLEM)
g.bind("lrmoo", LRMOO)


g.add((URIRef("https://w3id.org/golem/ontology/response/data#"), RDF.type, OWL.Ontology))
g.add((
    URIRef("https://w3id.org/golem/ontology/response/data#"),
    OWL.imports,
    URIRef("file:///Users/regina/Documents/UNIBO/Thesis/GOLEM/golem_ontology-reader_response/reader_response_module/development/03/it3_TBox.ttl")
))

DIG_OBJ = CRM_DIG.D1_Digital_Object
DIG_EVENT = CRM_DIG.D7_Digital_Machine_Event
DISCOURSE_ACT = RESPONSE_ONT.Discourse_Act
EXPRESSION = LRMOO.F2_Expression
THREAD = RESPONSE_ONT.Thread

HAS_TYPE = CRM.P2_has_type

# read the csv
with open("reader_response_module/development/03/it3_data_model.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:
        #obj type 
        obj_uri = RESPONSE_DATA[row["obj_id"].strip()]
        if row["obj_type"] == "Expression":
            g.add((obj_uri, RDF.type, EXPRESSION))
        else:
            g.add((obj_uri, RDF.type, DISCOURSE_ACT))
            g.add((obj_uri, HAS_TYPE, RESPONSE_ONT[row["discourse_type"].strip()]))
            if row["discourse_theme"]:
                g.add((obj_uri, RESPONSE_ONT.has_theme, RESPONSE_ONT[row["discourse_theme"].strip()]))
            if row["discourse_sentiment"]:
                g.add((obj_uri, RESPONSE_ONT.has_sentiment, RESPONSE_ONT[row["discourse_sentiment"].strip()]))
            if row["responds_to"]:
                g.add((obj_uri, RESPONSE_ONT.responds_to, RESPONSE_DATA[row["responds_to"].strip()]))
        if row["part_of"]:
            g.add((obj_uri, CRM.P148i_is_component_of, RESPONSE_DATA[row["part_of"].strip()]))
        g.add((obj_uri, SCHEMA.text, Literal(row["obj_text"].strip())))

        #expression
        if row["subject_id"]:
            subj_uri = RESPONSE_DATA[row["subject_id"].strip()]
            g.add((subj_uri, RDF.type, EXPRESSION))
            g.add((subj_uri, SCHEMA.title, Literal(row["title"].strip())))
            g.add((obj_uri, CRM.P129_is_about, subj_uri))

        #golem entities
        if row["golem_element"]:
            entity_id = row["golem_element"].split("|")[0].strip()
            golem_type = row["golem_element"].split("|")[1].strip()
            g.add((RESPONSE_DATA[entity_id], RDF.type, GOLEM[golem_type]))
            g.add((obj_uri, CRM.P67_refers_to, RESPONSE_DATA[entity_id]))

        #digital object
        if row["dig_obj_id"]:
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
            user_uri = RESPONSE_DATA[row["actor_id"].strip()]
            g.add((user_uri, RDF.type, RESPONSE_ONT.User))
            if row["actor_role"]:
                g.add((user_uri, RESPONSE_ONT.has_user_role, RESPONSE_ONT[row["actor_role"].strip()]))

            #digital object and action
            dig_uri = RESPONSE_DATA[row["dig_obj_id"].strip()]
            g.add((dig_uri, RDF.type, DIG_OBJ))
            g.add((dig_uri, RESPONSE_ONT.encoded_by, webpage_uri))
            g.add((dig_uri, SCHEMA.datePublished, Literal(row["date_published"].strip(), datatype=XSD.date)))

            g.add((dig_uri, RESPONSE_ONT.encodes, obj_uri))
            g.add((obj_uri, RESPONSE_ONT.encoded_by, dig_uri))

            action_uri = RESPONSE_DATA[f'{row["obj_id"].strip()}_Action']
            g.add((action_uri, RDF.type, DIG_EVENT))
            g.add((action_uri, CRM.P14_carried_out_by, user_uri))
            g.add((user_uri, CRM.P14i_performed, action_uri))
            g.add((action_uri, CRM_DIG.L11_had_output, dig_uri))

            if row["action_type"] == "UserPosts":
                g.add((action_uri, HAS_TYPE, RESPONSE_ONT.UserPosts))
                g.add((dig_uri, HAS_TYPE, RESPONSE_ONT.Post))
            else:
                g.add((action_uri, HAS_TYPE, SCHEMA.UserComments))
                g.add((dig_uri, HAS_TYPE, SCHEMA.Comment))

            if row["upvote_count"]:
                g.add((dig_uri, RESPONSE_ONT.upvoteCount, Literal(int(row["upvote_count"].strip().replace(",", "")), datatype=XSD.integer)))

            if row["like_count"]:
                g.add((dig_uri, RESPONSE_ONT.likeCount, Literal(int(row["like_count"].strip().replace(",", "")), datatype=XSD.integer)))

            #thread object
            if row["thread_id"]:
                thread_uri = RESPONSE_DATA[row["thread_id"].strip()]
                g.add((thread_uri, RDF.type, THREAD))
                g.add((thread_uri, HAS_TYPE, RESPONSE_ONT[row["thread_type"].strip()]))
                g.add((thread_uri, RESPONSE_ONT.has_comment, dig_uri))
                g.add((dig_uri, RESPONSE_ONT.is_comment_of, thread_uri))


# save
g.serialize(destination="reader_response_module/development/03/it3_ABox.ttl", format="turtle")
print("RDF file successfully saved as 'it3_ABox.ttl'")