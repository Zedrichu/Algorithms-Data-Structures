#include <bits/stdc++.h>
using namespace std;

struct Stack {
    int top, size;
    int* arr;

    Stack(int c) {
        top = -1;
        size = c;
        arr = new int;
    }

    bool isEmpty() {
        return (top == -1);
    }

    bool isFull() {
        return (top == size - 1);
    }

    int peek() {
        if (isEmpty()) throw "Stack is empty!";
        return arr[top];
    }

    void push(int x) {
        if (isFull()) throw "Stack is full!";
        arr[++top] = x;
    }

    int pop() {
        if (isEmpty()) throw "Stack is empty!";
        return arr[top--];
    }

    bool contains(int x) {
        if (isEmpty()) throw "Stack is empty!";
        for (int i=top; i>=0; i--) {
            if (arr[i] == x) return true;
        }
        return false;
    }
};


int main()
{
    Stack S(4);
    S.push(2);
    S.push(3);
    cout<<(bool)S.contains(2)<<endl;
    cout<<S.peek()<<endl;
    return 0;
}
