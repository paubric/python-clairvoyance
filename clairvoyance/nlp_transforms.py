import Algorithmia
import pprint

algorithmia_key = 'simUTMULmOWj/OpAO9AUMXk+sFX1'

def string_to_len(graph, nodes):
    print('Performing transform string_to_len on nodes: ', nodes)

    input_type = 'string'
    output_type = 'integer'
    transform_results = []

    for node in nodes:
        if (graph.nodes[node]['type'] == input_type):
            transform_results.append(len(node))
        else:
            print('Incompatible types')
            return (-1, -1)

    return transform_results, output_type

def string_to_word_count(graph, nodes):
    print('Performing transform string_to_word_count on nodes: ', nodes)

    input_type = 'string'
    output_type = 'integer'
    transform_results = []

    for node in nodes:
        if (graph.nodes[node]['type'] == input_type):
            transform_results.append(len(node.split()))
        else:
            print('Incompatible types')
            return (-1, -1)

    return transform_results, output_type

def string_to_gender(graph, nodes):
    print('Performing transform string_to_gender on nodes: ', nodes)

    input_type = 'string'
    output_type = 'string'
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

    input_type = 'string'
    output_type = 'string'
    transform_results = []

    for node in nodes:
        if (graph.nodes[node]['type'] == input_type):
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

    input_type = 'string'
    output_type = 'string'
    transform_results = []

    for node in nodes:
        if (graph.nodes[node]['type'] == input_type):
            client = Algorithmia.client(algorithmia_key)
            algo = client.algo('nlp/AutoTag/1.0.1')
            result = algo.pipe(node)
            transform_results.append(' '.join(result.result))
        else:
            print('Incompatible types')
            return (-1, -1)

    return transform_results, output_type

def string_to_sentiment(graph, nodes):
    print('Performing transform string_to_sentiment on nodes: ', nodes)

    input_type = 'string'
    output_type = 'number'
    transform_results = []

    for node in nodes:
        if (graph.nodes[node]['type'] == input_type):
            client = Algorithmia.client(algorithmia_key)
            algo = client.algo('nlp/SentimentAnalysis/1.0.4')
            result = algo.pipe({'document':node})
            transform_results.append(result.result[0]['sentiment'])
        else:
            print('Incompatible types')
            return (-1, -1)

    return transform_results, output_type
