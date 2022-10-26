/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    struct ListNode* new=NULL;

    if(list1==NULL)
        return(list2);     
    else if(list2==NULL)
        return(list1);
    else if(list1==NULL&&list2==NULL)
        return NULL;
        
    if(list1->val<=list2->val){
            new=list1;
            new->next=mergeTwoLists(new->next,list2);
        }
    else{
            new=list2;
            new->next=mergeTwoLists(list1,new->next);
        }
        
    return(new);
}