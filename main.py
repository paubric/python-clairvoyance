from clairvoyance import core, nlp_transforms, net_transforms, entity_types
import matplotlib.pyplot as plt
import networkx as nx

sentence = 'Jim went to Stanford University, Tom went to the University of Washington. They both work for Microsoft.'
name = 'Jane'
ip = '172.217.18.78'
domain = 'google.com'

G = core.Graph()
G.add_entity(ip, entity_types.ip_type())
G.add_entity(domain, entity_types.domain_type())

G.make_transform([ip], net_transforms.ip_to_country)
G.make_transform([domain], net_transforms.domain_to_ip)
"""
G.make_transform([name], nlp_transforms.string_to_len)
G.make_transform([sentence], nlp_transforms.string_to_word_count)
G.make_transform([name], nlp_transforms.string_to_gender)
G.make_transform([sentence], nlp_transforms.string_to_sentiment)
G.make_transform([sentence], nlp_transforms.string_to_tags)
"""

print('\n')
print(G.graph.nodes())
print(G.graph.nodes().data())
plt.subplot(111)
nx.draw_random(G.graph, with_labels=True)
plt.show()
