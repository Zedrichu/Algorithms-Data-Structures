#include <bits/stdc++.h>
using namespace std;

class QuickFind{
    vector<int> ids;
    int size;

    public:
        QuickFind(int N){
            ids = vector<int>(N);
            for (int i=0;i<N;i++)
                ids[i] = i;
            size = N;
        }

        int find(int i) {
            return ids[i];
        }

        void qunion(int i, int j){
            int iID = find(i);
            int jID = find(j);
            if (iID != jID)
                for (int k=0;k<size;k++)
                    if (ids[k] == iID)
                        ids[k] = jID;
            
        }
};

int main() {
    int N,M;
    cin>>N;
    cin>>M;
    QuickFind qf = QuickFind(N);
    for (int i=0;i<M;i++){
        char c;
        cin>>c;
        if (c=='F'){
            int x;
            cin>>x;
            cout<<qf.find(x)<<endl;
        } else if (c=='U') {
            int x,y;
            cin>>x>>y;
            qf.qunion(x,y);
        }
    }
}