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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* curr = head;
        int count=0;
        while(curr){
            curr=curr->next;
            count++;
        }
        ListNode* curr2=head;
        ListNode* prev = nullptr;
        int count2=0;
        if(count-n==0){
            return head->next;
        }
        while(curr2){
            if(count2==count-n){
                prev->next = curr2->next;
                break;
            }
            prev = curr2;
            curr2 = curr2->next;
            count2++;
        }
        return head;
    }
};
