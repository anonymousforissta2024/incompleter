#Source: https://stackoverflow.com/questions/61365330/celery-running-signature-from-database-attributeerror-object-has-no-attribute
import json
from celery.canvas import Signature
flatten = jsonpickle.pickler.Pickler().flatten
restore = jsonpickle.unpickler.Unpickler().restore

def signature_dumps(obj: Signature) -> str:
    """
    Serialize celery signature object to string
    :param obj: celery.canvas:Signature
    :return: str
    """
    return json.dumps(flatten(obj), indent=2)


def signature_loads(s: str) -> Signature:
    """
    Create celery signature object from string value
    :param s: string representation of signature
    :return: celery.canvas:Signature object
    """
    return restore(json.loads(s))