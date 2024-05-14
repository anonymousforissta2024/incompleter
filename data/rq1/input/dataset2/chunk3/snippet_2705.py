#Source: https://stackoverflow.com/questions/65586172/sqlalchemy-object-throwing-attribute-error-for-sa-instance-state-in-pytest
class TestConfig(Config):                                                                                                                                   
    TESTING = True                                                                                                                                          
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'                                                                                                           
    WTF_CSRF_ENABLED = False                                                                                                                                
    BCRYPT_LOG_ROUNDS = 4                                                                                                                                   
                                                                                                                                                            
def fill_database():                                                                                                                                        
    s0 = Source(title='Catalist')                                                                                                                           
    s1 = Source(title='L2')                                                                                                                                 
    sources = [s0, s1]                                                                                                                                      
    l0 = Voterlist(description='Test List 0')                                                                                                               
    l1 = Voterlist(description='Test List 1')                                                                                                               
    lists = [l0, l1]                                                                                                                                        
    return lists, sources                                                                                                                                   
                                                                                                                                                            
@pytest.fixture(scope='class')                                                                                                                              
def test_client():                                                                                                                                          
    flask_app = create_app(TestConfig)                                                                                                                      
    with flask_app.test_client() as client:                                                                                                                 
        app_context = flask_app.test_request_context()                                                                                                      
        app_context.push()                                                                                                                                  
        db.create_all()                                                                                                                                     
        lists, sources = fill_database()                                                                                                                    
        for s in sources:                                                                                                                                   
            db.session.add(s)                                                                                                                               
            db.session.commit()                                                                                                                             
        for l in lists:                                                                                                                                     
            db.session.add(l)                                                                                                                        
            db.session.commit()                                                                                                                             
            sleep(1)                                                                                                                                        
        yield client                                                                                                                                        
        db.drop_all()                                                                                                                                       
    app_context.pop() 