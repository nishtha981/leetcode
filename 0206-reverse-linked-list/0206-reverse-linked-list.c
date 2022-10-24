/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head){
    
    struct ListNode *prev=NULL;
    struct ListNode *new=NULL;
    while(head!=NULL)
    {
        new=head->next;
        head->next=prev;
        prev=head;
        head=new;
    }
    head=prev;
    return head;

}