#include <bits/stdc++.h>
using namespace std;

struct Node {
    int data;
    Node * next;
    Node(int x) {
        data = x;
        next = NULL;
    }
};


struct Stack {
    Node* top;

    Stack() {top = NULL;}
    
    bool isEmpty() {
        return (top == NULL);
    }

    //Peek element at S - head of stack (linked list)
    int Peek() {
        if (isEmpty()) throw "Stack is empty!";
        return top->data;
    }

    //Contains query in stack S
    bool Contains(int x) {
        Node * iter = top; 
        while (iter->next and iter->data != x) 
            iter = iter->next;   
        return (iter->data == x);
    }
    
    //Pop element at S - head of linked list
    int Pop() { 
        if (isEmpty()) throw "Stack is empty!";
        Node * q = top;
        top = top->next;
        int val = q->data;
        delete q;
        return val;    
    }

    //Push element before S - head of linked list
    void Push(int x){ 
        Node* q = new Node(x);
        if (top) {
            q->next = top; 
            top = q; 
        } else top = q;
    }
};

// <| Test Block |>
// int main() {
//     Stack S;
//     S.Push(2);
//     S.Push(3);
//     cout<<(bool)S.Contains(2)<<endl;
//     cout<<S.Peek()<<endl;
// }

// <| Problem Block |>
int main() {
    int n=0;
    cin>>n;
    string b;
    getline(cin,b);
    Stack S;
    for (int i=0;i<n;i++) {
        string str="";
        getline(cin,str);
        if (str[0]=='P'){
            if (str[1]=='U') {
                S.Push(stoi(str.substr(3,str.find('\n'))));
            } else if (str[1]=='O') {
                cout<<S.Pop()<<endl;
            }
        }
    }
    return 0;
};
