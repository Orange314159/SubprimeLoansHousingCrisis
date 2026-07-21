import textwrap ## actual life saver
import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

nodes = {
    'A': 'Housing Insecurity',

    'B': 'Number Loans Subprime',
    'C': '% of Housing owned\nby Private Equity',
    'D': '% total city tax revenue\nmade up by property taxes',
    'E': '% land within tract zoned\nfor single family home only',
    'F': 'Average Political Stance',
    'G': 'Voter Participation Rates',
    'H': 'Number of rent controlled\nunits per capita',
    'I': 'U6 Unemployment',
    'J': 'Average Income',
    'K': 'New Units Constructed\nper Capita',
    'L': 'Average Credit Score',
    'M': 'Indebtedness Ratio',
    'N': 'Income Inequality',
    'O': 'Difference in\n2010 / 2020 Census',
    'P': '% White',
    'Q': '% Married',
    'R': '% LGBTQ+',
    'S': '% with College Degree',
    'T': 'Average Children @ Home',
    'U': 'Rural / Suburban / Urban',

    'a': '2004 - 2007 Loans',
    'b': 'Current Rates of\nPrivate Equity',
    'c': 'Local Political\nConsiderations',
    'd': 'Economic Indicators',
    'e': 'Population Growth / Loss',
    'f': 'Demographic Considerations'
}

for node_id, label in nodes.items():
    G.add_node(node_id, label=label)

edges = [
    ('A', 'a'), ('A', 'b'), ('A', 'c'), ('A', 'd'), ('A', 'e'), ('A', 'f'), ## head to sub node 
    ('a', 'B'), ('b', 'C'), ('c', 'D'), ('c', 'E'), ('c', 'F'), ('c', 'G'), ('c', 'H'), 
    ('d', 'I'), ('d', 'J'), ('d', 'K'), ('d', 'L'), ('d', 'M'), ('d', 'N'),
    ('e', 'O'), ('f', 'P'), ('f', 'Q'), ('f', 'R'), ('f', 'S'), ('f', 'T'), ('f', 'U')
]

G.add_edges_from(edges)


## split these into some on top and some on bottom so it has a reasonable h to w ratio 
top_leaves = ['B', 'C', 'D', 'E', 'F', 'G', 'H']          
top_cats = ['a', 'b', 'c']   

main_node = ['A']                     

bottom_cats = ['d', 'e', 'f']                           
bottom_leaves = ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U']

pos = {}

def set_layer_pos(layer_nodes, y_val):
    ## space the nodes out evenly
    n = len(layer_nodes) ## total length 
    for idx, node in enumerate(layer_nodes): 
        x_val = (idx + 0.5) / n ## equal spacing
        pos[node] = (x_val, y_val) ## add to list

## must do for each row
set_layer_pos(top_leaves, 1.0)
set_layer_pos(top_cats, 0.75)
set_layer_pos(main_node, 0.50)
set_layer_pos(bottom_cats, 0.25)
set_layer_pos(bottom_leaves, 0.0)

fig, ax = plt.subplots(figsize=(18, 14))

## edges 
nx.draw_networkx_edges(
    G, pos, ax=ax, ## connect to mpl
    edge_color='#888888', ## dark
    arrows=True,
    arrowstyle='->',
    arrowsize=14,
    node_size=0,
    connectionstyle="arc3,rad=0.03" ## idk what this means but found it online in documentation somewhere
)



for node, (x, y) in pos.items():
    label_text = nodes[node]
    
    ## ... i just love text wrap...
    wrapped_text = "\n".join(textwrap.wrap(label_text, width=16))
    
    ## use red, green, blue, for the colors of the different nodes  
    if node == 'A':
        box_color = '#ffb3b3'
        font_weight = 'bold'
        font_size = 8
    elif node in top_cats or node in bottom_cats:
        box_color = '#b3e6b3'  
        font_weight = 'bold'
        font_size = 7
    else:
        box_color = '#e6f2ff'
        font_weight = 'normal'
        font_size = 6

    ax.text(
        x, y, wrapped_text,
        ha='center', va='center',
        fontsize=font_size,
        fontweight=font_weight,
        bbox=dict(
            boxstyle='round,pad=0.5',
            facecolor=box_color,
            edgecolor='#444444', ## less dark
            linewidth=1.2
        )
    )

## final plot things 
plt.title("Subprime Loan Analysis DAG", fontsize=14, fontweight='bold', pad=20)
plt.axis('off')
plt.tight_layout()
plt.savefig("subprime_loan_analysis_vertical.png", dpi=300, bbox_inches='tight')
plt.show()

