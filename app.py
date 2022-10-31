"""
AttackWeb .01 pre-alpha

Pyvis implementation inspired by Khuyen Tran:
https://towardsdatascience.com/pyvis-visualize-interactive-network-graphs-in-python-77e059791f01

Pyvis Network library adjusted to work with Python 3.7+ and included as pyvisfix_network.py

"""
from flask import Flask, render_template
import pandas as pd
from pyvisfix_network import Network
app = Flask(__name__)


# Select data and display preferences for Attack Graph output
def draw_network(nodes: list, df: pd.DataFrame, minium_weight: int = 0,
                 repulsion: int = 100, spring_length=200):
    """
    Builds network object data, enables probabilities and visualisation
    :param nodes: list of nodes from Excel via pandas
    :param df: dataframe from pandas
    :param minium_weight: min probability for graph
    :param repulsion: physics setting for distance between nodes
    :param spring_length: length of links between nodes
    :return: network object from pyvisfix_network
    """
    net = Network("600px", "800px", notebook=True)
    net.add_nodes(nodes)

    # add edges
    for node, weights in df.iterrows():
        edges = get_edges(node, weights, nodes, minium_weight)
        net.add_edges(edges)

    # change node distance and spring length
    net.repulsion(repulsion, spring_length=spring_length)

    return net


# Create edges between nodes
def get_edges(node: str, weights: list, all_nodes: list, minium_weight: int):
    """
    Builds the edges from nodes
    :param node: taken from Excel file
    :param weights: probabilities from the Excel file
    :param all_nodes: list of all nodes from pandas
    :param minium_weight: threshold for graphing (e.g., ignore 0 probability)
    :return: list of edge dictionary objects
    """
    nodes = all_nodes.copy()

    # Remove target node
    nodes.remove(node)

    # Create a list of edges with weights
    edges = [(node, connection, weight) for connection, weight in zip(nodes, weights)]

    # Get only edges with weights greater than the minimum weight
    edges = [edge for edge in edges if edge[2] >= minium_weight]

    return edges


# Use pandas to ingest Attack Tree data
df = pd.read_excel('excel/target.xlsx', index_col=0)

# extract nodes from ingest file
nodes = df.columns.to_list()
nodes = [node.strip() for node in nodes]

net = draw_network(nodes, df, minium_weight=1, repulsion=100, spring_length=100)


@app.route('/')
def plot():
    """
    Builds template that houses graph visualisation and list of probabilities
    :return: plot template and list of edge dictionary objects
    """
    edge_list = net.get_edges()

    return render_template('plot.html', edge_list=edge_list)


@app.route('/graph', methods=['GET', 'POST'])
def graph():
    """
    Builds a visualisation in HTML with Pyvis/VisJS package
    :return: either a stand-alone HTML file if notebook=False, or iFrame if notebook=True
    """

    net.write_html("templates/new_graph.html", notebook=True)

    return render_template('new_graph.html')


if __name__ == "__main__":
    app.run(debug=False)
