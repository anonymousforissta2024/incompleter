#Source: https://stackoverflow.com/questions/60849825/typeerror-kollision-missing-1-required-positional-argument-self
class score():
    def __init__(self, pbaum):
        schrift = pygame.font.SysFont("OCR A" , 30 , True ) 
        self.Baum = pbaum

    def anzeigen(self):
        score = 0

        self.text = schrift.render("Score: " + str(score)  , 0 , (0,0,0))
        screen.blit(self.text , (550 , 10))  

#Objekt der Klasse Schlitten erzeugen
spieler1 = Schlitten(350,400,screen)
Score = score(Baum)
#Objekt der Klasse Baum erzeugen
Baum1 = Baum(500,0 ,screen , Schlitten)
Baum2 = Baum(300,-525 , screen , Schlitten)
Baum3 = Baum(100,-1050 , screen, Schlitten)



schrift = pygame.font.SysFont("comicsans" , 30 , True ) 
# -------- Haupt-Schleife -----------
while not done:
    # Ändert den Wert von done auf True, falls Spiel-Fenster geschlossen wird
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    # --- hier Zeichenbefehle ergänzen---

    # Screen mit weiß fuellen
    screen.fill((255,255,255))

    pygame.mixer.music.set_volume(0.1)



    Score.anzeigen()


    # Schlitten zeichnen
    spieler1.zeichne_dich()
    spieler1.movemint()




    # Baeume zeichnen
    Baum1.zeichne()
    Baum1.bewegung()
    Baum1.spawn()
    Baum1.collision()




    Baum2.zeichne()
    Baum2.bewegung()
    Baum2.spawn()
    Baum2.collision()




    Baum3.zeichne()
    Baum3.bewegung()
    Baum3.spawn()
    Baum3.collision()









    # Maximale fps angeben
    clock.tick(60)

    # Bildschirm updaten um gezeichnete Objekte darzustellen
    pygame.display.flip()

# Pygame beenden, nachdem Haupt-Schleife beendet wurde
pygame.quit()