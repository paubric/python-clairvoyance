# Clairvoyance
Modular microframework which performs some basic data mining operations by generating directed graphs through a number of transforms. It works mostly by leveraging the power of third-party public APIs.

## Background
An open API (often referred to as a public API) is a publicly available application programming interface that provides developers with programmatic access to a proprietary software application or web service. Combining free public APIs from **data processing** services like Algorithmia, **social networks** like Twitter, **geolocators** like Google etc. results in a useful swiss army knife for data mining.

## Usage
After you import the `clairvoyance.core`, `clairvoyance.entity_types` and transform packages, you can create an instance of a graph and perform operations with it. Let's create an instance.
```
G = core.Graph()
```
Let's add a node in the graph, an entity called `Jane` of type `string`.
```
G.add_entity('Jane', entity_types.name_type())
```
Now let's perform a `string_to_gender` transform.
```
G.make_transform(['Jane'], nlp_transforms.string_to_gender)
```
Now the graph should contain another node, which is connected with the initial node. Performing multiple operations we can reach this:
![Demo](https://github.com/paubric/python-clairvoyance/blob/master/Figure_2.png)

## Transforms
### Available Transforms
- **nlp_transforms.string_to_len** - Get length of string
- **nlp_transforms.string_to_word_count** - Get number of words from strings
- **nlp_transforms.string_to_gender** - Get gender of name
- **nlp_transforms.string_to_tags** - Get relevant tags from text <s>(TO DO implement one-to-many)</s>
- **nlp_transforms.string_to_summary** - Get summarized version of text
- **nlp_transforms.string_to_named_entities** - Get named entities from text
- **nlp_transforms.string_to_languages** - Get language of text
- **net_transforms.ip_to_domain** - Get dns domain from ip address
- **net_transforms.ip_to_location** - Get country from ip address
- **net_transforms.domain_to_ip** - Get ip address from dns domain

A transform has the following structure and it can be easily integrated: 
```
def intype_to_outtype(graph, nodes):
    print('Performing transform intype_to_outtype on nodes: ', nodes)

    input_type = entity_types.intype()
    output_type = entity_types.outtype()
    transform_results = []

    for node in nodes:
        if (graph.nodes[node]['type'] == input_type):
            transform_results.append(singular_transform(node))
        else:
            print('Incompatible types')
            return (-1, -1)

    return transform_results, output_type
```
## Entity Types
### Available Entity Types
- **string_type**
    - **lang_type**
    - **name_type**
    - **domain_type**
    - **ip_type**
    - **country_type**
- **integer_type**
- **float_type**

An entity type has the following structure and it can be easily integrated: 
```
def entity_type():
    return ['primitive type', 'specific subtype']
```
## TODO
- code refactoring
- add edge labels (generated transform name)
- <s>rethink entity types (primitive types (e.g. float), specific subtypes(e.g. temperature))</s>
- <s>implement one-to-many node transforms</s>
- more transforms:
    - natural language processing
        - <s>string_to_len</s>
        - <s>string_to_word_count</s>
        - <s>string_to_gender</s>
        - <s>string_to_summary</s>
        - <s>string_to_tags</s>
        - <s>string_to_named_entities</s>
        - string_to_translated
        - <s>string_to_language</s>
    - computer vision
        - image_to_faces
        - image_to_sentiment
        - image_to_tags
        - image_to_objects
    - social transforms:
        - string_to_tweets
        - user_to_tweets
    - network: 
        - <s>ip_to_location</s>
        - <s>ip_to_domain</s>
        - <s>domain_to_ip</s>
- improve(implement) visualization
