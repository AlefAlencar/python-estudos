import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Faz uma chamada de API e armazena a resposta
url = 'https://api.github.com/search/repositories?q=language:python&sorts=stars'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Armazena a resposta da API em uma variável
response_dict = r.json()
print(f'Total repositories: {response_dict["total_count"]}')

# Explora informações sobre os repositórios
repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')

'''# Analisa o primeiro repositório
repo_dict = repo_dicts[0]
print(f'\nKeys: {len(repo_dict)}')
for key in sorted(repo_dict.keys()):
    print(key)'''


'''print("\nSelected information about first repository:")
names, stars = [], []
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    names.append(repo_dict['name'])
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    stars.append(repo_dict['stargazers_count'])
    print(f"Repository: {repo_dict['html_url']}")
    # print(f"Created: {repo_dict['created_at']}")
    # print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
print(repo_dict)'''

'''print("\nSelected information about each repository:")
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])'''

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {'value': repo_dict['stargazers_count'],
                 'label': repo_dict['description'],
                 'xlink': repo_dict['html_url']}
    plot_dicts.append(plot_dict)

# CRIA A VISUALIZAÇÃO
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', plot_dicts)  # chart.add('', stars)

chart.render_to_file('python_repos30.svg')
