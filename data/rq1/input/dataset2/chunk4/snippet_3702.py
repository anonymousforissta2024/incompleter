#Source: https://stackoverflow.com/questions/61480481/python-class-attribute-error-although-the-attribute-is-present
class Enemy(Character):
     def __int__(self,char_name,char_desc):
         super().__int__(char_name,char_desc)
         self.hit_points = 0
         self.melee_strengths = {
             'Normal damage': None,
             'Piercing damage': None,
             'Bludgoning damage': None}
         self.special_strengths = {
             'Acid damage': None,
             'Cold damage': None,
             'Heat damage': None,
             'Holy damage': None,
             'Undead damage': None}
     def set_melee_strength(self, norm_str, pierce_str, bludge_str):
         self.melee_strengths['Normal damage'] = norm_str
         self.melee_strengths['Piercing damage'] = pierce_str
         self.melee_strengths['Bludgoning damage'] = bludge_str