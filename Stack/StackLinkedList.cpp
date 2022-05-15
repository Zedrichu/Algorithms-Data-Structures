#include <bits/stdc++.h>
using namespace std;

struct Node {
    int data;
    Node * next;
};

typedef Node * Stack;

bool isEmpty(Stack S) {
    if (S==NULL) return true;
    return false;
}

//Pop element at S - head of linked list
int Pop(Stack &S) { 
    if (isEmpty(S)) throw "Stack is empty!";
    Node * q = S;
    S = S->next;
    int val = q->data;
    delete q;
    return val;    
}

//Push element before S - head of linked list
void Push(Stack &S, int x){ 
    Node * q = new Node;
    q->next = NULL;
    q->data = x;
    if (S) {
        q->next = S; 
        S = q; 
    } else S = q;
}

int main() {
    int n=0;
    cin>>n;
    string b;
    getline(cin,b);
    Stack S = NULL;
    for (int i=0;i<n;i++) {
        string str="";
        getline(cin,str);
        if (str[0]=='P'){
            if (str[1]=='U') {
                Push(S, stoi(str.substr(3,str.find('\n'))));
            } else if (str[1]=='O') {
                cout<<Pop(S)<<endl;
            }
        }
    }
    return 0;
};
