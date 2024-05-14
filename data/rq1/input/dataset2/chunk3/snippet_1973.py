#Source: https://stackoverflow.com/questions/47886482/typeerror-str-object-is-not-callable-using-python-click-library
@click.command('my_command', 'Initialize my_command')
@click.option('--s1', type=click.STRING, envvar='S_1',
              help='s1')
@click.option('--s2', type=click.STRING, envvar='S_2',
              help='s2')
@click.option('--i', type=click.STRING, envvar="I")
@click.option('--c', type=click.STRING, envvar="C")
@click.option('--l', default='[]', type=click.STRING, envvar="L")
@click.option('--st', default='[]', type=click.STRING, envvar="ST")
@click.option('--s', default='[]', type=click.STRING, envvar="S")
def my_command(s1, s2, i, c, l, st, s):
    ...