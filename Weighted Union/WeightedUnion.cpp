#include <bits/stdc++.h>
using namespace std;

class WeightedUnion{
    vector<int> p,sz;
    public:
        WeightedUnion(int N) {
            p = vector<int>(N);
            sz = vector<int>(N);
            for (int i=0;i<N;i++){
                p[i] = i;
                sz[i] = 1;
            }
        }

        int find(int i){
            while(i != p[i]){
                i = p[i];
            }
            return i;
        }

        void wunion(int i, int j){
            int ri = find(i);
            int rj = find(j);
            if (ri != rj)
                if (sz[ri] < sz[rj]){
                    p[ri] = rj;
                    sz[rj] += sz[ri];
                } else {
                    p[rj] = ri;
                    sz[ri] += sz[rj];
                }
        }      
};


int main() {
    int N,M;
    cin>>N;
    cin>>M;
    WeightedUnion wu = WeightedUnion(N);
    for (int i=0;i<M;i++){
        char c;
        cin>>c;
        if (c=='F'){
            int x;
            cin>>x;
            cout<<wu.find(x)<<endl;
        } else if (c=='U') {
            int x,y;
            cin>>x>>y;
            wu.wunion(x,y);
        }
    }
}
