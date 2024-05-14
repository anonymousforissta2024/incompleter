#Source: https://stackoverflow.com/questions/73186251/typeerror-supertype-obj-obj-must-be-an-instance-or-subtype-of-type-during-m
class Google(GoogleTranslator, GoogleDrive):
  
  @staticmethod
  def translate(text: str, goal_language: str = "EN") -> Optional[str]:
    return super().translate(text, goal_language)

  @staticmethod
  def save_to_drive(text: str) -> str:
    return super().save_to_drive(text)