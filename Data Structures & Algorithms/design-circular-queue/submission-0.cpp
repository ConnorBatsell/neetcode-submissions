class MyCircularQueue {
private:
    int capacity;
    vector<int> queue;
public:
    MyCircularQueue(int k) {
        capacity=k;
    }
    
    bool enQueue(int value) {
        if(queue.size()==capacity){
            return false;
        }
        queue.push_back(value);
        return true;
    }
    
    bool deQueue() {
        if(queue.empty()){
            return false;
        }
        queue.erase(queue.begin());
        return true;
    }
    
    int Front() {
        if(isEmpty()){
            return -1;
        }
        return queue[0];
    }
    
    int Rear() {
        if(isEmpty()){
            return -1;
        }
        return queue[queue.size()-1];
    }
    
    bool isEmpty() {
        if(queue.size()==0){
            return true;
        }
        return false;
    }
    
    bool isFull() {
        if(queue.size()==capacity){
            return true;
        }
        return false;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */