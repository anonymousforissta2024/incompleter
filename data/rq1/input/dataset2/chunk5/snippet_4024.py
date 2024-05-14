#Source: https://stackoverflow.com/questions/50421623/python-3-tkinter-nameerror-name-price-overall-release-is-not-defined
price_overall_release = 0
# A definition for adding and subtracting to the price at the bottom.
def release_button(add_or_sub, game_id):
    global price_overall_release
    if add_or_sub == "add":
        price_releases[game_id] = float(price_releases[game_id])
        price_overall_release = price_overall_release + price_releases[game_id]
        price_releases[game_id] = str(price_releases[game_id])

        # Declare and show.
        price_overall_release = str(price_overall_release)
        label_overallprice_releases = Label(new_release_window, text="$"+price_overall_release,
                            bg = releases_price_colour, fg = "black", relief = "sunken", borderwidth = 1, font = gui_font_10)
        amount_ordered_release = Label(new_release_window, text = amount_release,
                            bg = releases_price_colour, fg = "black", borderwidth = 1, font = gui_font_10)

        label_overallprice_releases.grid(row = 12, column = 3, padx = 7.5, pady = space_between) # +
        price_overall_release = float(price_overall_release)

        return price_overall_release
    else:
        price_releases[game_id] = float(price_releases[game_id])
        price_overall_release = price_overall_release - price_releases[game_id]
        price_releases[game_id] = str(price_releases[game_id])

        # Declare and show.
        price_overall_release = str(price_overall_release)
        label_overallprice_releases = Label(new_release_window, text="$"+price_overall_release,
                            bg = releases_price_colour, fg = "black", relief = "sunken", borderwidth = 1, font = gui_font_10)

        label_overallprice_releases.grid(row = 12, column = 3, padx = 7.5, pady = space_between) # +
        price_overall_release = float(price_overall_release)

        return price_overall_release

# Buttons.
releases_button_colour_add = ("forestgreen")
releases_button_colour_sub = ("firebrick")
#   1._________ 
button_game1_add = Button(new_release_window, text = "+", bg = releases_button_colour_add, font = "Helvetica 10", fg = "white",
                      width = 2, command = lambda: release_button("add", 3))
button_game1_sub = Button(new_release_window, text = "-", bg = releases_button_colour_sub, font = "Helvetica 10", fg = "white",
                      width = 2, command = lambda: release_button("sub", 3))
#   2._________
button_game2_add = Button(new_release_window, text = "+", bg = releases_button_colour_add, font = "Helvetica 10", fg = "white",
                      width = 2, command = lambda: release_button("add", 4))
button_game2_sub = Button(new_release_window, text = "-", bg = releases_button_colour_sub, font = "Helvetica 10", fg = "white",
                      width = 2, command = lambda: release_button("sub", 4))