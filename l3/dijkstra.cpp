#include <iostream>
#include <stdio.h>
#include <queue>
#include <vector>
#include <limits>
#include "pqueue.hpp"
#include <fstream>
#include <string>
#include <array>
#include "dijkstra.hpp"

using namespace std;

Graph::Graph(int n, int m) {
    // Constructor with parameters
    this->n = n; // number of nodes
    this->m = m; // number of arcs
    index = 0;
    arcs = new int*[m]; // declare how many elements have the first dim
    nodes = new int[n];
    
    int nodesindex = 0;
    for (int i=0; i<n; i++) {
        nodes[i] = nodesindex + 1;
        nodesindex++; 
    }
    
    // clear value in array
    for (int i=0; i<m; i++) {
        arcs[i] = new int[3]; // declare how mamy elements have the second dim
    }
}

void Graph::show() {
    cout << "mam " << n << " wierzchołkow i " << m << " krawedzi" << endl;
        for (int i=0; i<m; i++) {
            cout << arcs[i][0] << " " << arcs[i][1] << " " << arcs[i][2] << endl;
        }
        for (int i=0; i<n; i++) {
            cout << nodes[i] << " ";
    }
}

void Graph::addArcs(int u, int v, int w) {
    // u and v is (u,v) acrs, where u is starting node and v in ending node
    if (index < m) {
        arcs[index][0] = u;
        arcs[index][1] = v;
        arcs[index][2] = w;
        index++;
    }
}

int* dijkstra(Graph *graph, int source, int d[]) {
    // int d[graph->n + 1];
    int pred[graph->n+1];
    
    for (int i=0; i<graph->n+1; i++) {
        d[i] = numeric_limits<int>::max();
        pred[i] = -1; // undef;
        // (*vertex) = numeric_limits<int>::max();
    }

    d[source] = 0;
    PriorityQueue* Q = new PriorityQueue;
    Q->insert(source, d[source]);

    while (!Q->isEmpty()) {
        Node* cur = Q->pop();
        for (int i=0; i<graph->m; i++) {
            if (graph->arcs[i][0] == cur->id) {
                if (d[graph->arcs[i][1]] > d[cur->id] + graph->arcs[i][2]) {
                    d[graph->arcs[i][1]] = d[cur->id] + graph->arcs[i][2];
                    pred[graph->arcs[i][1]] = cur->id;
                    Q->insert(graph->arcs[i][1], d[graph->arcs[i][1]]);
                }
            }
        }
    }

    // for (int i=0; i<graph->n+1; i++) {
    //     cout << i << " " << d[i] << " " << pred[i] << endl;
    // }

    return d;
    // if ( (int) (sizeof(vertex)/sizeof(*vertex)) != 0)  {
    //     int idx = 0;
    //     for (int i=1; i<graph->n + 1; i++) {
    //         if (i==vertex[idx]) {
    //             cout << i << " " << d[i] << " " << pred[i] << endl;
    //             idx++;
    //         }
    //     }
    // }
}

// int d[graph.n + 1];
//     int pred[graph.n+1];
    
//     for (int i=0; i<graph.n+1; i++) {
//         d[i] = numeric_limits<int>::max();
//         pred[i] = -1; // undef;
//     }

//     d[source] = 0;
//     PriorityQueue* Q = new PriorityQueue;
//     Q->insert(source, d[source]);

//     while (!Q->isEmpty()) {
//         Node* cur = Q->pop();
//         for (int i=0; i<graph.m; i++) {
//             if (graph.arcs[i][0] == cur->id) {
//                 if (d[graph.arcs[i][1]] > d[cur->id] + graph.arcs[i][2]) {
//                     d[graph.arcs[i][1]] = d[cur->id] + graph.arcs[i][2];
//                     pred[graph.arcs[i][1]] = cur->id;
//                     Q->insert(graph.arcs[i][1], d[graph.arcs[i][1]]);
//                 }
//             }
//         }
//     } 
    
    // for (int i=0; i<graph.n + 1; i++) {
    //     cout << i << " " << d[i] << " " << pred[i] << endl;
    // }

array<int, 3> split(string s){
    string delimiter = " ";
    array<int, 3> array;
    int counter = 0;

    if (s[0] == 'a') {
        size_t pos = 0;
        string token;
        while ((pos = s.find(delimiter)) != string::npos) {
            token = s.substr(0, pos);
            // cout << token << endl;
            array[counter] = atoi(token.c_str());
            counter++;
            s.erase(0, pos + delimiter.length());
        }
        // cout << s << endl;
        array[counter] = atoi(s.c_str());
    } else {
        array[0] = 0;
        array[1] = 0;
        array[2] = 0;
    }
    return array;
}


// int main() {
    // Graph graph(5, 10);
    // graph.addArcs(1,2,10);
    // graph.addArcs(1,3,5);
    // graph.addArcs(2,3,2);
    // graph.addArcs(3,2,3);
    // graph.addArcs(2,4,1);
    // graph.addArcs(3,5,2);
    // graph.addArcs(5,1,7);
    // graph.addArcs(3,4,9);
    // graph.addArcs(4,5,4);
    // graph.addArcs(5,4,6);

    // dijkstra(graph, 1);

    // Graph graph(5, 9);
    // graph.addArcs(1,2,4);
    // graph.addArcs(1,3,2);
    // graph.addArcs(2,4,2);
    // graph.addArcs(2,3,3);
    // graph.addArcs(3,2,1);
    // graph.addArcs(3,5,5);
    // graph.addArcs(3,4,4);
    // graph.addArcs(5,4,1);
    // graph.addArcs(2,5,3);

    // dijkstra(graph, 1);

    // ifstream myfile;
    // myfile.open("Random4-n.10.0.gr");
    // string mystring;
    // array<int, 3> splited;

    // if (myfile.is_open()) {
    //     // while (myfile) {
    //     for (int i=0; i<10; i++) {
    //         getline(myfile, mystring);
    //         // if (mystring[0] != 'a') {
    //         //     cout << mystring << "--" << endl;
    //         // }
    //         splited = split(mystring);

    //         for (int k=0; k<4;k++) {
    //             cout << splited[k] << "::";
    //         }
    //         cout << endl;
    //     }
    // }

    // split("siema mateusz to ja sie nazywam mateusz");

    

//     return 0; 
// }