import Algorithmia
from . import entity_types

algorithmia_key = 'simUTMULmOWj/OpAO9AUMXk+sFX1'

def string_to_len(graph, nodes):
    print('Performing transform string_to_len on nodes: ', nodes)

    input_type = entity_types.string_type()
    output_type = entity_types.integer_type()
    transform_results = []

    for node in nodes:
        if (graph.nodes[node]['type'][0] == input_type[0]):
            transform_results.append(len(node))
        else:
            print('Incompatible types')
            return (-1, -1)

    return transform_results, output_type

def string_to_word_count(graph, nodes):
    print('Performing transform string_to_word_count on nodes: ', nodes)

    input_type = entity_types.string_type()
    output_type = entity_types.integer_type()
    transform_results = []

    for node in nodes:
        if (graph.nodes[node]['type'][0] == input_type[0]):
            transform_results.append(len(node.split()))
        else:
            print('Incompatible types')
            return (-1, -1)

    return transform_results, output_type

def string_to_gender(graph, nodes):
    print('Performing transform string_to_gender on nodes: ', nodes)

    input_type = entity_types.name_type()
    output_type = entity_types.string_type()
    transform_results = []

    for node in nodes:
        if (graph.nodes[node]['type'] == input_type):
            client = Algorithmia.client(algorithmia_key)
            algo = client.algo('barend/Genderize/0.1.3')
            result = algo.pipe(node)
            transform_results.append(result.result['gender'])
        else:
            print('Incompatible types')
            return (-1, -1)

    return transform_results, output_type

def string_to_summary(graph, nodes):
    print('Performing transform string_to_summary on nodes: ', nodes)

    input_type = entity_types.string_type()
    output_type = entity_types.string_type()
    transform_results = []

    for node in nodes:
        if (graph.nodes[node]['type'][0] == input_type[0]):
            client = Algorithmia.client(algorithmia_key)
            algo = client.algo('nlp/Summarizer/0.1.7')
            result = algo.pipe(node)
            transform_results.append(result.result)
        else:
            print('Incompatible types')
            return (-1, -1)

    return transform_results, output_type

def string_to_tags(graph, nodes):
    print('Performing transform string_to_tags on nodes: ', nodes)

    input_type = entity_types.string_type()
    output_type = entity_types.string_type()
    transform_results = []

    for node in nodes:
        if (graph.nodes[node]['type'][0] == input_type[0]):
            client = Algorithmia.client(algorithmia_key)
            algo = client.algo('nlp/AutoTag/1.0.1')
            result = algo.pipe(node)
            transform_results.append(result.result)
        else:
            print('Incompatible types')
            return (-1, -1)

    return transform_results, output_type

def string_to_sentiment(graph, nodes):
    print('Performing transform string_to_sentiment on nodes: ', nodes)

    input_type = entity_types.string_type()
    output_type = entity_types.float_type()
    transform_results = []

    for node in nodes:
        if (graph.nodes[node]['type'][0] == input_type[0]):
            client = Algorithmia.client(algorithmia_key)
            algo = client.algo('nlp/SentimentAnalysis/1.0.4')
            result = algo.pipe({'document':node})
            transform_results.append(result.result[0]['sentiment'])
        else:
            print('Incompatible types')
            return (-1, -1)

    return transform_results, output_type

def string_to_named_entities(graph, nodes):
    print('Performing transform string_to_named_entities on nodes: ', nodes)

    input_type = entity_types.string_type()
    output_type = entity_types.string_type()
    transform_results = []

    for node in nodes:
        if (graph.nodes[node]['type'][0] == input_type[0]):
            client = Algorithmia.client(algorithmia_key)
            algo = client.algo('StanfordNLP/NamedEntityRecognition/0.2.0')
            result = algo.pipe(node)
            result = [item[0] for item in result.result[0]]
            transform_results.append(result)
        else:
            print('Incompatible types')
            return (-1, -1)

    return transform_results, output_type

def string_to_language(graph, nodes):
    print('Performing transform string_to_language on nodes: ', nodes)

    input_type = entity_types.string_type()
    output_type = entity_types.lang_type()
    transform_results = []

    for node in nodes:
        if (graph.nodes[node]['type'][0] == input_type[0]):
            client = Algorithmia.client(algorithmia_key)
            algo = client.algo('nlp/LanguageIdentification/1.0.0')
            result = algo.pipe(node)
            print(result.result)
            transform_results.append(result.result)
        else:
            print('Incompatible types')
            return (-1, -1)

    return transform_results, output_type
