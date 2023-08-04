#include <bits/stdc++.h>
using namespace std;

struct Node {
    int data;
    Node * next;
    Node (int x) {
        data = x;
        next = NULL;
    }
};

struct Queue
{
    Node* tail;
    Node* head;

    Queue() {tail = head = NULL;}

    bool isEmpty() {
        return (head == NULL);
    }

    int peek() {
        return head->data;
    }

    bool contains(int value) {
        Node* iter = head;
        while (iter->next and iter->data != value) {
            iter = iter->next;
        }
        return (iter->data == value);
    }

    void enqueue(int x) {
        Node * q = new Node(x);
        if (!tail) {
            head = q;
            tail = q;
        }
        tail->next = q;
        tail = q;
    }

    int dequeue() {
        if (!head) {
            return NULL;
        }
        
        Node * q = head;
        head = head->next;
        
        if (!head) tail = NULL;

        int val = q->data;
        delete q;
        return val;
    }
};

// <| Test Block |>
// int main() {
//     Queue Q;
//     Q.enqueue(2);
//     Q.enqueue(3);
//     Q.enqueue(1);
//     cout<<Q.peek()<<endl;
//     cout<<Q.dequeue()<<endl;
//     cout<<Q.contains(2)<<endl;
//     cout<<Q.contains(3)<<endl;
// }

// <| Problem Block |>
int main() {
    int n=0;
    cin>>n;
    string b;
    getline(cin,b);
    Queue Q;
    for (int i=0;i<n;i++) {
        string str="";
        getline(cin,str);
        if (str[0]=='E') {
            Q.enqueue(stoi(str.substr(2,str.find('\n'))));
        } else if (str[0]=='D') {
            cout<<Q.dequeue()<<endl;
        }
    }
    return 0;
}
