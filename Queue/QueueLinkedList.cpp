#include <bits/stdc++.h>
using namespace std;

struct Node {
    int data;
    Node * next;
};

typedef Node * Queue;

int dequeue(Queue &head, Queue &tail) {
    if (head == tail) {
        int val = head->data;
        delete head;
        return val;
    } else {
        Node * q = head;
        while (q->next != tail) {q=q->next;}
        int val = tail->data;
        delete tail;
        q->next = NULL;
        tail = q;
        return val;
    }
}

void enqueue(Queue &head, Queue &tail, int x) {
    Node * q = new Node;
    q-> next = head;
    q-> data = x;
    if (!head) tail = q;
    head = q;
}

int main() {
    int n=0;
    cin>>n;
    string b;
    getline(cin,b);
    Queue head = NULL, tail = NULL;
    for (int i=0;i<n;i++) {
        string str="";
        getline(cin,str);
        if (str[0]=='E') {
            enqueue(head, tail, stoi(str.substr(2,str.find('\n'))));
        } else if (str[0]=='D') {
            cout<<dequeue(head, tail)<<endl;
        }
    }
    return 0;
}
