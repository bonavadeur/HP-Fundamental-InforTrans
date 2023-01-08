#include <iostream>
#include <cmath>
#include <queue>
using namespace std;
struct MinHeapNode {
    char data;
    double freq;
    MinHeapNode* left, *right;
    MinHeapNode(char data, double freq)
    {
        left = right = NULL;
        this->data = data;
        this->freq = freq;
    }
};
struct compare{
    bool operator()(MinHeapNode* l, MinHeapNode* r)
    {
        return (l->freq > r->freq);
    }
};
struct result {
    string data;
    string* binary = new string[100];
    double avgLength = 0;
    double Entropy = 0;
};
result rs; //bien output
int idx = 0;
void output(MinHeapNode* root, string str) {
    if (!root)
        return;
    if (root->data != '$') {
    		rs.data[idx] = root->data;
	        rs.binary[idx] = str;
	        rs.avgLength += root->freq * str.length();
	        rs.Entropy += -(root->freq * log2(root->freq));
			idx++;
    }
    output(root->left, str + "0");
    output(root->right, str + "1");
}
void HuffmanCodes(char data[], double freq[], int size)
{
    MinHeapNode* left, * right, * top;
    priority_queue<MinHeapNode*, vector<MinHeapNode*>, compare> minHeap;
    for (int i = 0; i < size; ++i)
        minHeap.push(new MinHeapNode(data[i], freq[i]));
    while (minHeap.size() != 1) {
        left = minHeap.top();
        minHeap.pop();
        right = minHeap.top();
        minHeap.pop();
        top = new MinHeapNode('$', left->freq + right->freq);
        top->left = left;
        top->right = right;
        minHeap.push(top);
    }
    output(minHeap.top(), "");
}
int main()
{
    char arr[] = { 'a', 'b', 'c', 'd', 'e', 'f'};
    double freq[] = {0.28, 0.22, 0.16, 0.15, 0.14, 0.05};
    int size = sizeof(arr) / sizeof(arr[0]);
    HuffmanCodes(arr, freq, size);
    for(int i = 0; i < size; i++){
    	cout << rs.data[i] << ": " << rs.binary[i] << endl;
	}
	cout << rs.avgLength << " " << rs.Entropy;
}
