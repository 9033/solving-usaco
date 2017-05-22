/*
PROG: fence6
ID: kkangne001
LANG:C++11
*/
#include<fstream>
#include<unordered_set>
#include<vector>
using namespace std;
int segment_len[101] = {0,16,3,3,8,8,6,5,4,5,10};
int min_meter = 255*100+1;
unsigned int start =0;

vector< unordered_set<int> > nodes;
int nodes_mark[999];

int dfs(unsigned int point, int meter, int depth=0){
    if( meter > min_meter)return 0;
    if( start == point && meter > 0){
        min_meter = min( meter, min_meter);
        return 0;
    }
    for(unsigned int next=0;next<nodes.size();next++){
        if(next!=point){
            for(unsigned int cross_seg : nodes[point]){
                if( nodes[next].count(cross_seg) && nodes_mark[cross_seg] == 0 ){ //the other end?
                    nodes_mark[cross_seg] = 1;
                    dfs(next, meter+segment_len[cross_seg],depth+1);
                    nodes_mark[cross_seg] = 0;
                }
            }
        }
    }   

    return 0;
}

int main(){
    fstream fin("fence6.in", fstream::in);
    fstream fout("fence6.out", fstream::out);
    int N;
    fin >> N;

    for(int n=1;n<=N;n++){
        int num, len, N1, N2;
        fin >> num >> len >> N1 >> N2;         
        segment_len[num] = len;         

        auto f1 = [&](int Ni) {
            unordered_set<int> newnode;
            newnode.insert(num);
            for(int i = 0;i<Ni;i++){
                int j;
                fin >> j;
                newnode.insert(j);
            }
            int f=0;
            for(auto & i : nodes){
                if( newnode == i){
                    f =1;
                }
            }
            if(f==0)nodes.push_back( newnode );
            return 0;
        };
        f1(N1);
        f1(N2);
    }

    for(start = 0;start<nodes.size();start++){
        dfs(start,0);
    }
    fout << min_meter << endl;
    return 0;
}
