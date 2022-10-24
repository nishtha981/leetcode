/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeElements(struct ListNode* head, int val)
{
    struct ListNode* new;
    if(head==NULL)
        return NULL;
    if(head->val==val)
        return removeElements(head->next,val);
    new=head;
    while(new->next!=NULL)
        if(new->next->val==val)
          new->next=new->next->next;
    else new=new->next;
    return head;
}