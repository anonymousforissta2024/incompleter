#Source: https://stackoverflow.com/questions/57656994/attributeerror-parent-variable-variable-user-id-dtype-numeric-is-not-t
es = es.entity_from_dataframe(entity_id="train", 
                              dataframe=df_es_train,
                              index="impression_id",
                              time_index="impression_time",
                              )

es = es.entity_from_dataframe(entity_id="viewlogs", 
                              dataframe=df_es_view_logs,
                              index="index",
                              time_index="server_time",
                              )

es = es.entity_from_dataframe(entity_id="itemdata", 
                              dataframe=df_es_item_data,
                              index="item_id",
                              )

new_relationship_1 = ft.Relationship(es["itemdata"]["item_id"],
                                   es["viewlogs"]["item_id"])
es = es.add_relationship(new_relationship_1)
new_relationship = ft.Relationship(es["train"]["user_id"],
                                   es["viewlogs"]["user_id"])
es = es.add_relationship(new_relationship)