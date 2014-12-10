

# Tree is a general concept, even a single node is also a tree
class TREE:
    
#     def __init__(self, v, depth, time):
#         self.v_children=[]
#         self.v_value=v
#         self.v_depth=depth
#         self.v_size=1
#         self.v_time=time

    def __init__(self, v, depth):
        self.v_children=[]
        self.v_value=v
        self.v_depth=depth
        self.v_size=1
        
        self.set=[]
        #self.v_time=time

    def root(self):
        #this function create all tables
        return self
    
    def depth(self):
        return self.v_depth
    
    
    def value(self):
        return self.v_value
    
    
    def time(self):
        return self.v_time
    
    # add a tree as a child of the current tree
    def addChild(self, tree):
        self.v_children.append(tree)

    
    def treeDepth(self):
        depth=0
        
        for k in self.v_children:
            t = k.treeDepth()
            if t>depth:
                depth=t
        return depth+1
        
    def treeSize(self):
        size=0
        
        for k in self.v_children:
            t = k.treeSize() 
            size += t
        return size + self.v_size
    
    
    def treeSet(self):
        if len(self.set) >0:
            return self.set
        else:
            ret=[self.v_value]
        
            for k in self.v_children:
                t = k.treeSet() 
                ret += t
            return ret        
    
    def node(self, v):
        if self.v_value == v:
            return self
        else:
            for k in self.v_children:
                found = k.node(v)
                if found != None:
                    return found
        return None    
    
    
    # calculate the ratio of childrennum over the friendsNum
    def stepProb(self, s_sql, steps):
        fn = s_sql.friendsNumU(self.value())
#        if fn==0:
#            rate=0
#        else:
#            rate = float(len(self.v_children))/fn
            
        if self.v_depth not in steps.keys():
            steps[self.v_depth]=[[len(self.v_children)],[fn]]
        else:
            steps[self.v_depth][0].append(len(self.v_children))
            steps[self.v_depth][1].append(fn)                              
        
        for i in self.v_children:
            i.stepProb(s_sql, steps)
        
    
    

def main():
    root=TREE(5)
    root.addChild(TREE(8))
    root.addChild(TREE(9))
    root.addChild(TREE(10))
    root.node(8).addChild(TREE(20))
    root.node(8).addChild(TREE(21))
    root.node(20).addChild(TREE(30))
    root.node(20).addChild(TREE(31))

    print root.treeDepth(), root.treeSize(), root.set()
    
if __name__ == '__main__':
    main()   
        