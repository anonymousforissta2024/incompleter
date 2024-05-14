#Source: https://stackoverflow.com/questions/65333888/attributeerror-int-object-has-no-attribute-model
import csv
import random
import genanki

# Filename of the data file
data_filename = str(input("Enter input file name with extension: "))

# Filename of the Anki deck to generate
deck_filename = data_filename.split('.')[0] + ".apkg"

# Title of the deck as shown in Anki
anki_deck_title = data_filename.split('.')[0]

# Name of the card model
anki_model_name = "Modelname"

# Create the deck model

model_id = random.randrange(1 << 30, 1 << 31)

style = """
.card {
 font-family: arial;
 font-size: 24px;
 text-align: center;
 color: black;
 background-color: white;
"""

anki_model = genanki.Model(
    model_id,
    anki_model_name,
    fields=[{"name": "front"}, {"name": "back"}],
    templates=[
        {
            "name": "Card 1",
            "qfmt": '{{front}}',
            "afmt": '{{FrontSide}}<hr id="answer">{{back}}</p>',
        },
    ],
    css=style,
)

# The list of flashcards
anki_notes = []

with open(data_filename, "r", encoding="utf-8") as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=";")

    for row in csv_reader:
        anki_note = genanki.Note(
            model=anki_model,
            fields=[row[0], row[1]]
        )
        anki_notes.append(anki_note)

for subdeck in range(int((round((len(anki_notes)/1000)+0,5)))):
  anki_deck = genanki.Deck(model_id, anki_deck_title+" "+str((subdeck-1)*1000+1)+"-"+str(subdeck*1000))
  anki_package = genanki.Package(anki_deck)

  # Add flashcards to the deck
  for anki_note in range(1000):
      anki_deck.add_note(anki_note)

  # Save the deck to a file
  anki_package.write_to_file(deck_filename)
  print("Created deck with {} flashcards".format(len(anki_deck.notes)))