#include <bits/stdc++.h>
using namespace std;

class QuickUnion{
    vector<int> p;

    public:
        QuickUnion(int N){
            p = vector<int>(N);
            for (int i=0;i<N;i++){
                p[i] = i;
            }
        }

        int find(int i) {
            while (i != p[i]){
                i = p[i];
            }
            return i;
        }

        void qunion(int i, int j){
            int ri = find(i);
            int rj = find(j);
            if (ri != rj) 
                p[ri] = rj;
        }
};

int main() {
    int N,M;
    cin>>N;
    cin>>M;
    QuickUnion qu = QuickUnion(N);
    for (int i=0;i<M;i++){
        char c;
        cin>>c;
        if (c=='F'){
            int x;
            cin>>x;
            cout<<qu.find(x)<<endl;
        } else if (c=='U') {
            int x,y;
            cin>>x>>y;
            qu.qunion(x,y);
        }
    }
}
