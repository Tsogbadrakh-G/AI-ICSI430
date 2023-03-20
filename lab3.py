
from queue import PriorityQueue
romania_map = (dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Zerind=dict(Arad=75,Oradea=71),
    Sibiu=dict(Arad=140,Rimnicu=80,Oradea=151,Fagaras=80),
    Fagaras=dict(Sibiu=99, Bucharest=211),
    Timisoara=dict(Arad=118,Lugoj=111),
    Oradea=dict(Zerind=71, Sibiu=151),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Mehadia=dict(Lugoj=70,Drobeta=75),
    Drobeta=dict(Mehadia=75,Craiova=120),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Pitesti=dict( Bucharest=101,Rimnicu=97,Craiova=138),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Giurgiu=dict(Bucharest=90),
    Rimnicu=dict(Sibiu=80,Pitesti=97,Craiova=146),
    Urziceni=dict(Vaslui=142,Bucharest=85,Hirsova=98),
    Eforie=dict(Hirsova=86),
    Hirsova=dict(Urziceni=98,Eforie=86),
    Iasi=dict(Vaslui=92, Neamt=87),
    Neamt=dict(Iasi=87),
    Vaslui=dict(Iasi=92, Urziceni=98)))




def dfs(adj,s,res):

    parent={}
    len1=0
   # len2=-1
   # parent={}
    for s in romania_map:
        if s not in parent:
            parent[s]=None
            print(parent)
            dfs_visit(adj,s,len1,parent,res)
        
    


def dfs_visit(adj,s,len1,parent,res):
     #print(parent)
     for v in adj[s]:
         
         
         if v not in parent:
             len1+=adj[s][v]
            # print(len1)
            # print(v)
             if v=='Bucharest':
            
                res.append(len1)
                len1=0
             parent[v]=s
             dfs_visit(adj,v,len1,parent,res) 
     


def bfs(adj,s):
    len=0
    level={s:0}
    parent={s:None}
    i=1
    state=0
    frontier=[s] #frontier=['Arad']
    print('bfs:')
    
    while frontier:
        next=[]
      #  print('1')
        for u in frontier: # 'Arad'
        
            for v in adj[u]:
             #   print(adj[u][v])
              
                if v not in level:
                    len+=adj[u][v]
                    if v=='Bucharest':
                        
                        state=1
                        break
                    level[v]=i
                    parent[v]=u
                    next.append(v)
                
            if(state==1): break
        if(state==1): break
        frontier=next
        i+=1

    return len


def init(romania_map):
    graph = {}

    for key in romania_map:
        temp = []
        for key2 in romania_map[key]:
            temp.append(key2)
            if(key2 not in romania_map):
                temp2 = []
                for key3 in romania_map:
                    if key2 in romania_map[key3]:
                        temp2.append(key3)
                graph[key2] =temp
        graph[key] = temp
    return graph

#adj=init(romania_map)
def Djikstra(V, s,adj):
    D={v:float('inf') for v in V}
    D[s]=0
    S=list()
    Q= PriorityQueue()
    Q.put((0, s))
    
    while not Q.empty():
        (dist, u) =Q.get()
        S.append(u)

        for neighbor in adj[u]:
           
                distance = adj[u][neighbor]
                if neighbor not in S:
                    old_cost = D[neighbor]
                    new_cost = D[u] + distance
                    if new_cost < old_cost:
                        Q.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

print('bfs result:')
res=bfs(romania_map,'Arad')
print(res)
ret=list()
print('dfs result:')
dfs(romania_map,'Arad',ret)
print(ret.pop(0))

V=[v for v in romania_map]
print('djikstra result:')
resp=Djikstra(V,'Arad',romania_map)
print(resp['Bucharest'])
def test(adj, s):
    for v in adj[s]:
        print(v)

#test(romania_map,'Giurgiu')
