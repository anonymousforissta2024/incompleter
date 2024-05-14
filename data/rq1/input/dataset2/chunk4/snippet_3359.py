#Source: https://stackoverflow.com/questions/73186251/typeerror-supertype-obj-obj-must-be-an-instance-or-subtype-of-type-during-m
class AbsTranslator(ABC):
  @abstractmethod
  def translate(text: str, goal_language: str) -> Optional[str]:
    pass

class AbsDrive(ABC):
  @abstractmethod
  def save_to_drive(text: str) -> None:
    pass