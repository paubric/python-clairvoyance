from clairvoyance import core, nlp_transforms
import matplotlib.pyplot as plt
import networkx as nx

sentence = 'best algorithm ever!'

G = core.Graph()
G.add_entity('Jane', 'string')
G.add_entity(sentence, 'string')

G.make_transform(['Jane'], nlp_transforms.string_to_len)
G.make_transform(['Jane'], nlp_transforms.string_to_gender)
G.make_transform([sentence], nlp_transforms.string_to_word_count)
G.make_transform([sentence], nlp_transforms.string_to_tags)
G.make_transform([sentence], nlp_transforms.string_to_sentiment)

print('\n')
print(G.graph.nodes())
nx.draw_random(G.graph, with_labels=True)
plt.show()
