#include <unordered_map>
using namespace std;

class LRUCache {
private:
    struct ListNode {
        int ke;
        int va;
        ListNode* next;
        ListNode* prev;

        ListNode(int k, int v)
            : ke(k), va(v), next(nullptr), prev(nullptr) {}
    };

    int space;
    unordered_map<int, ListNode*> mp;

    // Dummy head and tail
    ListNode* left;   // LRU side
    ListNode* right;  // MRU side

    void remove(ListNode* node) {
        ListNode* p = node->prev;
        ListNode* n = node->next;

        p->next = n;
        n->prev = p;
    }

    void insert(ListNode* node) {
        // Insert before right (most recently used)
        ListNode* p = right->prev;

        p->next = node;
        node->prev = p;

        node->next = right;
        right->prev = node;
    }

public:
    LRUCache(int capacity) {
        space = capacity;

        left = new ListNode(0, 0);
        right = new ListNode(0, 0);

        left->next = right;
        right->prev = left;
    }

    int get(int key) {
        if (mp.find(key) == mp.end())
            return -1;

        ListNode* node = mp[key];

        // Move to MRU position
        remove(node);
        insert(node);

        return node->va;
    }

    void put(int key, int value) {
        if (mp.find(key) != mp.end()) {
            // Remove old node
            remove(mp[key]);
            delete mp[key];
        }

        ListNode* node = new ListNode(key, value);
        mp[key] = node;

        insert(node);

        // Evict LRU if over capacity
        if (mp.size() > space) {
            ListNode* lru = left->next;

            remove(lru);
            mp.erase(lru->ke);

            delete lru;
        }
    }
};
