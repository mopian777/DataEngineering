#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Number of donors
#define N 10

int main() {
    int graph[N];
    srand(time(NULL)); // Initialize random number generator

    // Initialize graph with individual donations
    for (int i = 0; i < N; i++) {
        graph[i] = rand() % 10 + 1; // Random donation between 1 and 10
    }

    // Combine donations until all nodes are children
    int numNodes = N;
    while (numNodes > 1) {
        // Randomly select two nodes
        int parent = rand() % numNodes;
        int child = rand() % numNodes;
        while (child == parent) {
            child = rand() % numNodes; // Ensure child is not the same as parent
        }

        // Combine donations
        graph[parent] += graph[child];

        // Remove child node from graph
        for (int i = child; i < numNodes - 1; i++) {
            graph[i] = graph[i + 1];
        }
        numNodes--;
    }

    // Print total sum of donations
    printf("Total sum of donations: %d\n", graph[0]);

    return 0;
}
