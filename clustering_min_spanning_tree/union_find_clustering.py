import sys

class UnionFind:
    def __init__(self,N):
        self.clusters = {key: key for key in range(N)} 
    def find(self,p):
        return self.clusters[p]
    def union(self,p,q):
        _i = self.clusters[p] 
        _j = self.clusters[q] 

        if _i != _j :
            for inx in self.nclusters:
                if self.nclusters[inx] == _j:
                    self.nclusters[inx] = _i 


def kruskal_MST(E):
    sortedE = sorted(E, key = lambda x:x[2])
    T = set()
    uf = UnionFind(len(sortedE))
    for vert1,vert2, weight in sortedE:
        if uf.find(vert1) != uf.find(vert2):
            uf.union(vert1,vert2)
            T.add((vert1,vert2,weight))
    
    return T     
    


class  Cluster:
    def __init__(self,nclusters,data):
        self.nclusters = nclusters
        self.data = data 
        #self.max_spacing = []
    def cluster(self):
        
        edges= sorted(self.data , key = lambda x:x[2])
        #while(len(set(self.nclusters.values())) > 5):
        for i,j,w in edges:
            _i = self.nclusters[i]
            _j = self.nclusters[j]
            if _i != _j:
                for inx in self.nclusters:
                    if self.nclusters[inx] == _j :
                        self.nclusters[inx] = _i 
                       
            # label all together the same label  
            #self.max_spacing.append(w)
            #print(len(set(self.nclusters.values())))
            #print(self.nclusters.values())
            if len(set(self.nclusters.values())) == 4: break 
        cross_edges =[e[2] for e in edges if self.nclusters[e[0]] != self.nclusters[e[1]]]      
        return self.nclusters,min(cross_edges)
if __name__ == "__main__":
    data = [] ; nodes = set()
    with open('clustering1.txt') as f:
        for row in f:
            rows = row.strip().split() 
            if len(rows)<2 : continue
            data.append((int(rows[0]),int(rows[1]),int(rows[2])))
            nodes.add(int(rows[0]));nodes.add(float(rows[1])) 

    nclusters = dict()
    nclusters = {key: key for key in nodes} 
    job = Cluster(nclusters,data)
    rst1,max_spacing = job.cluster()
    print(set(rst1.values()))
    print(max_spacing)

    
    
