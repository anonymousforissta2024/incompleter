#Source: https://stackoverflow.com/questions/65586172/sqlalchemy-object-throwing-attribute-error-for-sa-instance-state-in-pytest
class ListAPI(Resource):                                                                                                                                    
    def __init__(self):                                                                                                                                     
        self.reqparse = reqparse.RequestParser()                                                                                                            
        self.fields = ['description', 'vendorquery', 'campaign', 's3key',                                                                                   
                       'ftimestamp', 'fname', 'source', 'user']                                                                                             
        for f in self.fields:                                                                                                                               
            self.reqparse.add_argument(f,                                                                                                                   
                                       type=str,                                                                                                            
                                       location='json')                                                                                                     
        super(ListAPI, self).__init__()                                                                                                                     
                                                                                                                                                            
    def get(self):                                                                                                                                          
        """Returns all lists."""                                                                                                                            
        try:                                                                                                                                                
            alllists = Voterlist.query.all()                                                                                                                
            lists = []                                                                                                                                      
            for l in alllists:                                                                                                                              
                l = l.__dict__                                                                                                                              
                l.pop('_sa_instance_state', None)                                                                                                           
                lists.append(l)                                                                                                                             
            return jsonify({'lists': lists})                                                                                                                
        except Exception as e:                                                                                                                              
            print(e)                                                                                                                                        
            abort(400, str(e)) 