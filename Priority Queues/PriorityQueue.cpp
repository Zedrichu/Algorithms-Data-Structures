#include <bits/stdc++.h>
using namespace std;

class PriorityQueue{
    vector<int> heap;
    int size;

    public:
        PriorityQueue() {
            heap = vector<int>();
            heap.push_back(0);
            size = 0;
        }

        bool less(int i, int j){
            return i>=1 && i<=size
                && j>=1 && j<=size
                && heap[i] < heap[j];
        }

        void swap(int i, int j){
            if (i!=0 && j!=0) {
                int temp = heap[i];
                heap[i] = heap[j];
                heap[j] = temp;
            }
        }

        void bubbleDown(int i){
            int left = 2*i;
            int child = left + less(left,left+1);
            if (less(i,child)) {
                swap(i,child);
                bubbleDown(child);
            }
        }

        void bubbleUp(int i){
            int parent = i/2;
            if (less(parent,i)){
                swap(parent,i);
                bubbleUp(parent);
            }
        }

        int max(){
            return heap[1];
        }

        void insert(const int &x){
            heap.push_back(x);
            size++;
            bubbleUp(size);
        }

        int extractMax() {
            int max = heap[1];
            heap[1] = heap[size];
            heap.pop_back();
            size--;
            bubbleDown(1);
            return max;
        }

        void print() {
            for (int i=0;i<size;i++){
                cout<<heap[i+1]<<' ';
            }
            cout<<endl;
        }

};

int main() {
    PriorityQueue pq = PriorityQueue();
    int N;
    cin>>N;
    for (int i=0;i<N;i++) {
        char c;
        cin>>c;
        if (c=='I'){
            int x;
            cin>>x;
            pq.insert(x);
        } else if (c=='E'){
            cout<<pq.extractMax()<<endl;
        } else if (c=='P'){
            pq.print();
        }
    }
}