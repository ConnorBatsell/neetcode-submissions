/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void reorderList(ListNode* head) {
        if(!head){
            return;
        }
        vector<ListNode*> nodes;
        ListNode* curr = head;
        while(curr){
            nodes.push_back(curr);
            curr=curr->next;
        }
        int i=0;
        int j = nodes.size()-1;
        while(i<j){
            ListNode* temp = nodes[i]->next;
            nodes[i]->next = nodes[j];
            nodes[j]->next = temp;
            i++;
            j--;
        }
        nodes[i]->next = nullptr;

    }
};
