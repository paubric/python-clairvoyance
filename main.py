from clairvoyance import core, nlp_transforms, entity_types
import matplotlib.pyplot as plt
import networkx as nx

sentence = 'Jim went to Stanford University, Tom went to the University of Washington. They both work for Microsoft.'
name = 'Jane'
G = core.Graph()
G.add_entity(name, entity_types.name_type())
G.add_entity(sentence, entity_types.string_type())

G.make_transform([sentence], nlp_transforms.string_to_language)
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
nx.draw_random(G.graph, with_labels=True)
plt.show()
