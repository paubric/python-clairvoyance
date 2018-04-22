import socket
from . import entity_types
import ipapi

def ip_to_domain(graph, nodes):
    print('Performing transform ip_to_domain on nodes: ', nodes)

    input_type = entity_types.ip_type()
    output_type = entity_types.domain_type()
    transform_results = []

    for node in nodes:
        if (graph.nodes[node]['type'] == input_type):
            result = socket.gethostbyaddr(node)
            transform_results.append(result[0])
        else:
            print('Incompatible types')
            return (-1, -1)

    return transform_results, output_type

def ip_to_country(graph, nodes):
    print('Performing transform ip_to_domain on nodes: ', nodes)

    input_type = entity_types.ip_type()
    output_type = entity_types.country_type()
    transform_results = []

    for node in nodes:
        if (graph.nodes[node]['type'] == input_type):
            result = ipapi.location(node)
            transform_results.append(result['country'])
        else:
            print('Incompatible types')
            return (-1, -1)

    return transform_results, output_type

def domain_to_ip(graph, nodes):
    print('Performing transform domain_to_ip on nodes: ', nodes)

    input_type = entity_types.domain_type()
    output_type = entity_types.ip_type()
    transform_results = []

    for node in nodes:
        if (graph.nodes[node]['type'] == input_type):
            result = socket.gethostbyaddr(node)
            transform_results.append(result[2])
        else:
            print('Incompatible types')
            return (-1, -1)

    return transform_results, output_type
