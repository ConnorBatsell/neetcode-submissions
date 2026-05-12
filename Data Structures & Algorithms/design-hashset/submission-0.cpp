class MyHashSet {
public:
    vector<int> myHashSet;

    MyHashSet() {
    }
    
    void add(int key) {
        if(!contains(key)){
            myHashSet.push_back(key);
        }
    }
    
    void remove(int key) {
        auto it = find(myHashSet.begin(), myHashSet.end(), key);
        if (it != myHashSet.end()) {
            myHashSet.erase(it);
        }    
    }
    
    bool contains(int key) {
        for(int i=0; i<myHashSet.size(); i++){
            if(myHashSet[i]==key){
                return true;
            }
        }
        return false;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */