#Source: https://stackoverflow.com/questions/61480481/python-class-attribute-error-although-the-attribute-is-present
dave = Enemy("Dave","A smelly zombie")
dave.describe()
dave.set_conversation('Be prepared to face my wrath')
dave.set_hit_points(50)
dave.set_melee_strength('neutral', 'resistant', 'weak')
dave.set_special_strength('neutral','neutral','neutral','weak','resistant')
dave.get_melee_strengths()
dave.get_special_strengths()