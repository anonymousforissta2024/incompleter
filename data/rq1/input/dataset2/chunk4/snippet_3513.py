#Source: https://stackoverflow.com/questions/68660137/why-does-presidio-stanzanlpengine-throw-nameerror-name-stanzalanguage-is-not
import stanza
stanza.download("en")

from presidio_analyzer.nlp_engine import StanzaNlpEngine
StanzaNlpEngine(models={"en": "en"})