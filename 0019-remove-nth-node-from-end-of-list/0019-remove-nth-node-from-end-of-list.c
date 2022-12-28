/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    
    if (head == NULL || n <= 0)
        return head;
    int len=0;
    struct ListNode* current = head;
    while (current != NULL) {
        len++;
        current=current->next;
    }
    if (n > len) 
        return head;
    
    int i =len - n;
    struct ListNode* prev = NULL;
    current=head ;
    while (i > 0) {
        prev = current;
        current=current->next;
        i--;
    }

    if (prev == NULL) 
        head = current->next;
    else 
        prev->next = current->next;
    
    free(current);
    return head;
}
