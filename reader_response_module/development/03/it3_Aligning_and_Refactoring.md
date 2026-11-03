# Iteration 3 - Alignment and Refactoring

With the digital framework established in the previous iteration, this iteration simply extends that with its discourse description. `Discourse_Act` is described as a subclass of `crm:E73_Information_Object` and connected to the digital object framework with the property `encoded_by`. As this property has as range any `crm:E73_Information_Object` this means it can also connect digital objects to creative expressions as described by the LRMoo class `F2_Expression`. Here the CRM property `P67_refers_to` and its subproperty, `P129_is_about`, are used to specify the subject of a discourse act. `P67_refers_to` is used specifically to describe the narrative features referred to by a discourse act. The description of these narrative features can then be classified by the GOLEM ontology classes. 

The new classes of `Discourse_Act_Type`, Discourse_Act_Theme (now renamed `Creative_Discourse_Theme`, for clarity), `Sentiment`, `Thread_Type` and `User_Role` are all declared as subclass of `crm:E55_Type` each with their respective type individuals. 

`Thread` is declared as a subclass of `crm:E73_Information_Object` with a specific restriction that is must contain at least one digital object with type comment. This is where the `has_comment` property will be used to specify this relationship.

Another thing to note is the use of both `responds_to` and `schema:parentItem`. `responds_to` will remain as a property on the discourse act level meaning that it describes the responsive relationship between discourse acts in general (regardless of their digital context). While `schema:parentItem` works on the digtial level, connecting a digital comment to either another digital comment or to a main digital post, similar to how its use is described on schema.org

A partial view of the of the model combining the digital framework and discourse framework can be seen below. 

<img width="4212" height="1821" alt="it3_full_model" src="https://github.com/user-attachments/assets/f4970dc6-6887-486c-9252-10c107739cae" />

