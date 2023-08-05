#include <bits/stdc++.h>
using namespace std;

struct Node {
    int key;
    Node * next, * prev;

    Node (int x) {
        key = x;
        next = prev = NULL;
    }
};

struct DoubleLinkedList {
    Node * head;

    DoubleLinkedList() { head = NULL; }

    bool IsEmpty() { 
        return (!head);
    }

    void Insert(int x) {
        Node * q = new Node(x);
        q->next = head;
        if (head) {
            head->prev = q;
        }
        head = q;
    }

    void Delete(Node * x) {
        if (x->prev) 
            x->prev->next = x->next;
        else 
            head = x->next;
        if (x->next)
            x->next->prev = x->prev;
    }

    Node * Search(int x) {
        Node * iter = head;
        while (iter) {
            if (iter->key == x) 
                return iter;
            iter = iter->next;
        }
        return NULL;
    }
};

int main() {
    DoubleLinkedList list;

    list.Insert(4);
    list.Insert(3);
    list.Insert(2);
    Node * node = list.Search(3);
    cout<<node->key<<endl; // Returns 3 
    cout<<list.head->next->next->key<<endl; // Returns 4
    list.Delete(node);
    cout<<list.head->key<<endl; // Returns 2
    cout<<list.head->next->key<<endl; // Returns 4
}