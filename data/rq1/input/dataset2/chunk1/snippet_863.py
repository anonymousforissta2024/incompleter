#Source: https://stackoverflow.com/questions/44004609/attributeerror-nonetype-object-has-no-attribute-decode
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        #'label': repo_dict['description'],
        'xlink': repo_dict['owner']['html_url'],
        }
    plot_dicts.append(plot_dict)