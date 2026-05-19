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
        ListNode* slow=head;
        ListNode* fast=head;
        while(fast && fast->next){
            slow=slow->next;
            fast=fast->next->next;
        }
        ListNode* curr=slow->next;
        slow->next = nullptr;
        ListNode* prev=nullptr;
        while(curr){
            ListNode* temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        ListNode* curr2=head;
        ListNode* second=prev;
        while(second){
            ListNode* temp = curr2->next;
            ListNode* temp2 = second->next;
            curr2->next = second;
            second->next = temp;
            curr2 = temp;
            second = temp2;
        }
        
    }
};
