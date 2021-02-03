import numpy as np
import sys


def get_new_graph(graph_canva_size = (10,10)):
    INF = np.inf
    graph_matrix = np.zeros(graph_canva_size)

    # input matrix size and number of paths
    n = None
    while n== None or n>10:
        n =  int(input("Please input graph size (<= 10):"))
        if n >=10:
            print("You should input a number is less than or equal to 10")
        

    # initialnize
    graph_matrix = np.delete(graph_matrix, np.s_[n::], axis =1)
    graph_matrix = np.delete(graph_matrix, np.s_[n::], axis =0)

    for node in range(n):
        for target in range(n):
            if node == target:
                graph_matrix[node][target] = 0
            else:
                graph_matrix[node][target] = INF
    
    return graph_matrix


def set_path_weight(graph):
    n =  int(input("Please input number of paths: "))
    
    print("Please input \"start node\", \"end_node\", \"path weight\": ")
    for path in range(n):
        start_node, end_node, weight = map(int, input().split(" "))
        graph[start_node][end_node] = weight
    
    return graph        

def launch_floyd(graph):
    for start_node in range(len(graph)):
        for target_node in range(len(graph)):
            for new_node in range(len(graph)):
                if graph[start_node][target_node]>graph[start_node][new_node] + graph[new_node][target_node]:
                    graph[start_node][target_node] = graph[start_node][new_node] + graph[new_node][target_node]
    return graph


#sample data
"""
8
0 1 4
0 3 8
1 2 3
2 3 4
2 4 2
3 2 4
3 4 8
4 1 7


零 --- 4 ---> 一
|            /^
|           3 |
|          /  |
8      二 <   7
|     ^ \     | 
|    4   2    |
|   /     \   |
V <        >  |
三 --- 8 ---> 四

"""

if __name__ == "__main__":
    graph = get_new_graph()
    print(graph)
    graph = set_path_weight(graph)
    print(graph)
    graph = launch_floyd(graph)
    print(graph)
    