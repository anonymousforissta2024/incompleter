#Source: https://stackoverflow.com/questions/73186251/typeerror-supertype-obj-obj-must-be-an-instance-or-subtype-of-type-during-m
class GoogleTranslator(AbsTranslator):
  @staticmethod
  def translate(text: str, goal_language: str) -> Optional[str]:
    return 'translatedText'

class GoogleDrive(AbsDrive):
  @staticmethod
  def save_to_drive(text: str) -> None:
    print('saving to drive...')