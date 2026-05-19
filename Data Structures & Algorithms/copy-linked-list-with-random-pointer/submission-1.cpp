/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
       unordered_map<Node*, Node*> temp;
       Node* curr=head;
       while(curr){
            temp[curr] = new Node(curr->val);
            curr = curr->next;
       }
        curr = head;
       while(curr){
            Node* copy = temp[curr];
            copy->next = temp[curr->next];
            copy->random = temp[curr->random];
            curr = curr->next;
       }
       return temp[head];
    }
};
