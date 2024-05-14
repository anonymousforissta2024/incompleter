#Source: https://stackoverflow.com/questions/54732607/attributeerror-module-utils-has-no-attribute-make-labels-in-featuretools-in
es = es.entity_from_dataframe(entity_id = 'orders',
                             dataframe = orders,
                             index = 'order_id',
                             variable_types = {

                                 'user_id' : ft.variable_types.Categorical,

                                 'eval_set' : ft.variable_types.Categorical,

                                 'order_number' : ft.variable_types.Numeric,

                                 'order_dow' : ft.variable_types.Numeric,

                                 'order_hour_of_day' : ft.variable_types.Numeric,

                                 'days_since_prior_order' : ft.variable_types.Numeric
                             })

es = es.entity_from_dataframe(entity_id = 'products',
                             dataframe = products,
                             index = 'product_id',
                             variable_types = {

                                 'product_name' : ft.variable_types.Categorical,

                                 'aisle_id' : ft.variable_types.Categorical,

                                 'department_id' : ft.variable_types.Categorical
                             })

es = es.entity_from_dataframe(entity_id = 'departments',
                             dataframe = departments,
                             index = 'department_id',
                             variable_types = {

                                 'department' : ft.variable_types.Categorical
                             })

es = es.entity_from_dataframe(entity_id = 'aisles',
                             dataframe = aisles,
                             index = 'aisle_id',
                             variable_types = {

                                 'aisle' : ft.variable_types.Categorical
                             })