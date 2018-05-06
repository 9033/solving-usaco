"""
ID: kkangne001
LANG: PYTHON3
TASK: ditch
"""
import math
io_filename = 'ditch'
#
fin = open (io_filename+'.in', 'r')
fout = open (io_filename+'.out', 'w')
#
fin_ints = lambda :[int(x) for x in fin.readline().split()]
array_2d = lambda M,I=0:[[I for i in range(M+1)] for j in range(M+1)]
array_1d = lambda M,I=0:[I for i in range(M+1)]
#

N,M = fin_ints()
max_flow = array_2d(M,0)

while N:
    a,b,c=fin_ints()
    max_flow[a][b]=c+max_flow[a][b]
    N=N-1

totalflow = 0
nil = -1
# 1 : source
# M : sink
while True:
    prevnode = array_1d(M,nil)
    flow = array_1d(M,-1)
    visited = array_1d(M,False)
    flow[1] = math.inf
    maxloc = nil
    while (True):
        maxflow = 0
        maxloc = nil
        #최대로 흘러오는 노드를 고름 (greedily 라고 나와있음)
        for i in range(1,M+1):
            if (flow[i] > maxflow) and (not visited[i]):
                maxflow = flow[i]
                maxloc = i
                
        if maxloc == nil:
            break
        if maxloc == M:
            break
            
        visited[maxloc] = True

        #인접한 노드에 저장된 이전에 계산한 최대치와 이 노드에서 흘러가는 양과 비교해서 갱신
        for i in range(1,M+1):
            if max_flow[maxloc][i] != -1:
                if (flow[i] < min(maxflow,max_flow[maxloc][i]) ):
                    prevnode[i] = maxloc
                    flow[i] = min(maxflow,max_flow[maxloc][i]) 

    if maxloc == nil:
        break

    pathcapacity = flow[M]
    totalflow = totalflow + pathcapacity 

    #반대방향으로 경로를 추가.
    curnode = M
    while curnode != 1:    
        nextnode = prevnode[curnode]
        max_flow[nextnode][curnode] = max_flow[nextnode][curnode] - pathcapacity
        max_flow[curnode][nextnode] = max_flow[curnode][nextnode] + pathcapacity
        curnode = nextnode
        

fout.write (str( totalflow ) + '\n')
fout.close()
#