#include <bits/stdc++.h>
using namespace std;

struct Queue {
    int front, rear, size;
    int* arr;

    Queue (int c) {
        size = c;
        front = 0;
        rear = -1;
        arr = new int;
    }

    bool isEmpty() {
        return (front == rear + 1);
    }

    bool isFull() {
        return ((rear - front) % size == size - 1);
    }

    int peek() {
        if (isEmpty()) throw "Queue is empty";
        return arr[front];
    }

    bool contains(int value) {
        if (isEmpty()) throw "Queue is empty!";
        int iter = front;
        while (iter != (rear + 1) % size) {
            if (arr[iter] == value) return true;
            iter = (iter + 1) % size;
        }
        return false;
    }

    void enqueue(int value) {
        if (isFull()) throw "Queue is full!";
        rear = (rear + 1) % size;
        arr[rear] = value;
    }

    int dequeue() {
        if (isEmpty()) throw "Queue is empty!";
        int x = arr[front];
        front = (front + 1) % size;
        return x;
    }
};

int main() {
    Queue Q(3);
    Q.enqueue(2);
    Q.enqueue(3);
    Q.enqueue(1);
    cout<<Q.peek()<<endl;
    cout<<Q.dequeue()<<endl;
    cout<<Q.contains(1)<<endl;
    cout<<Q.contains(2)<<endl;
}