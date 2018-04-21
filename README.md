# Clairvoyance
Modular microframework which generates directed graphs through a number of transforms, a primitive data mining program. It works mostly by leveraging the power of third-party public APIs.

## Background
An open API (often referred to as a public API) is a publicly available application programming interface that provides developers with programmatic access to a proprietary software application or web service. Combining free public APIs from data processing services like Algorithmia, social networks like Twitter, geolocators like Google etc. results in a useful swiss army knife for data mining.

## Usage
After you import the `clairvoyance.core` and `clairvoiyance.nlp_transforms`, you can create an instance of a graph and perform operations with it. Let's create an instance.
```
G = core.Graph()
```
Let's add a node in the graph, an entity called `Jane` entity of type `string`.
```
G.add_entity('Jane', 'string')
```
Now let's perform a `string_to_gender` transform.
```
G.make_transform(['Jane'], nlp_transforms.string_to_gender)
```
Now the graph should contain another node, which is connected with the initial node. Performing multiple operations we can reach this:
![Demo](https://github.com/paubric/python-clairvoyance/blob/master/Figure_2.png)
## TODO
