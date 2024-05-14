#Source: https://stackoverflow.com/questions/44004609/attributeerror-nonetype-object-has-no-attribute-decode
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['owner']['html_url'],
        }
    plot_dicts.append(plot_dict)

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Stared Python Project On Github'
chart.x_labels = names
chart.add('', plot_dicts)

chart.render_to_file('new_repos.svg')