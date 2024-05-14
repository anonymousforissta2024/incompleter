#Source: https://stackoverflow.com/questions/47064968/attributeerror-nonetype-object-has-no-attribute-foo
import player
Dice = random.randrange(1, 7)
set_p_w = player.set_player_weapon()
PlayerDamage = Dice * set_p_w.player_damage