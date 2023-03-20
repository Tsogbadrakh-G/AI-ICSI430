from queue import PriorityQueue
h=(dict(    
    Arad= 366,
 	Bucharest=0,
 	Craiova=160,
 	Dobreta=242,
 	Eforie=161,
 	Fagaras=176,
 	Giurgiu=77,
 	Hirsowa=151,
 	Lasi=226,
 	Lugoj=244,
 	Mehadia=241,
 	Neamt=234,
 	Oradea=380,
 	Pitesti=100,
 	Rimnicu=193,
 	Sibiu=253,
 	Timisoara=329,
 	Urziceni=80,
 	Vaslui=199,
 	Zerind=374))

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
def Greedy(rmap,h,s,nodes):
   min=float('inf')
   node=s
   nodes.append(s)
   for v in rmap[s]:
      if v=='Bucharest':
         node=v
         nodes.append(node)
         return nodes
         break
      elif(v not in nodes):
        if h[v] < min:
            min=h[v]
            node=v
      
   return Greedy(rmap,h,node,nodes)

def A_search(rmap,h,s,nodes,D):
   min=float('inf')
   node=s
   nodes.append(s)
   for v in rmap[s]:
      if v=='Bucharest':
         node=v
         nodes.append(node)
         return nodes
         break
      elif(v not in nodes):
         if h[v]+D[v] < min:
            min=h[v]+D[v]
            node=v
   print(h[node]+D[node])
   
   return A_search(rmap,h,node,nodes,D)

nodes1=list()
nodes2=list()
V=[v for v in romania_map]
d=Djikstra(V,'Arad',romania_map)
#print(d)
l0=A_search(romania_map,h,'Arad',nodes1,d)
print('A_search:')
print(l0)
print('Greedy:')
l=Greedy(romania_map,h,'Arad',nodes2)
print(l)