struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {

    struct ListNode start;
    start.next = head;
    struct ListNode* current = &start;
    struct ListNode* previous = &start;

    for (int i = 0; i <= n; i++) {
        current = current->next;
    }

    while (current != NULL) {
        current = current->next;
        previous = previous->next;
    }

    struct ListNode* temp = previous->next;
    previous->next = previous->next->next;
    free(temp);

    return start.next;
}
