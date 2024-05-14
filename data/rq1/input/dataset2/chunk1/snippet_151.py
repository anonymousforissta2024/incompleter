#Source: https://stackoverflow.com/questions/59298759/typeerror-nonetype-object-is-not-subscriptable-for-a-dictionary-in-my-game
def main():
    print(render_introduction())
    world = create_world()
    while world['status'] == 'playing':
        print(render(world))  #line 316
        options = get_options(world)
        command = choose(options)
        print(update(world, command))
    print(render_ending(world))
if __name__ == '__main__':
    main() #line323