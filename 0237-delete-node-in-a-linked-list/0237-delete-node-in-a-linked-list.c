/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void deleteNode(struct ListNode* node) {
    
    struct ListNode *prev=node;
    struct ListNode *after=node->next;
    prev->val=after->val;
    prev->next=after->next;
    after->next=NULL;
    free(after);
}