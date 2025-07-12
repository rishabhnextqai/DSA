import streamlit as st
import json
import random
from datetime import datetime, timedelta
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Master DSA 2025",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- GLOBAL STYLES & CUSTOM CSS ---
def set_custom_css():
    st.markdown(r'''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    :root {
        --font-family: 'Inter', sans-serif;
        --bg: #0D1117;
        --fg: #C9D1D9;
        --accent: #58A6FF;
        --card: #161B22;
    }
    html, body, [class*="st-"] {
        font-family: var(--font-family) !important;
        background-color: var(--bg) !important;
        color: var(--fg) !important;
    }
    .card {
        background: var(--card);
        border-radius: 16px;
        padding: 1rem;
        margin: 0.5rem 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5);
    }
    .btn-primary {
        text-transform: uppercase;
        font-weight: 600;
        color: #fff;
        background: var(--accent);
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
    }
    .btn-primary:hover { opacity: 0.9; }
    .sidebar-text { font-size: 1.1rem; padding: 0.5rem 0; }
    </style>
    ''', unsafe_allow_html=True)

set_custom_css()

# --- STATE MANAGEMENT ---
STATE_FILE = "dsa_progress.json"

def init_state():
    return {"completed": [], "notes": {}, "streak": 0, "last_date": None}

def load_state():
    if os.path.exists(STATE_FILE):
        try:
            return json.load(open(STATE_FILE))
        except:
            return init_state()
    return init_state()

def save_state(s):
    json.dump(s, open(STATE_FILE, "w"), indent=2)

if "state" not in st.session_state:
    st.session_state.state = load_state()

state = st.session_state.state

# --- JOURNEY DATA (14 weeks) ---
JOURNEY = [
    {
        "week": "Two Pointers and Fast & Slow pointers",
        "easy": [
            {"id": "w0-e0", "name": "Pair with Target Sum", "url": "https://leetcode.com/problems/two-sum/"},
            {"id": "w0-e1", "name": "Remove Duplicates", "url": "https://leetcode.com/problems/remove-duplicates-from-sorted-array/"},
            {"id": "w0-e2", "name": "Squaring a Sorted Array", "url": "https://leetcode.com/problems/squares-of-a-sorted-array/"},
            {"id": "w0-e3", "name": "LinkedList Cycle", "url": "https://leetcode.com/problems/linked-list-cycle/"},
            {"id": "w0-e4", "name": "Middle of the LinkedList", "url": "https://leetcode.com/problems/middle-of-the-linked-list/"},
        ],
        "medium": [
            {"id": "w0-m0", "name": "Triplet Sum to Zero", "url": "https://leetcode.com/problems/3sum/"},
            {"id": "w0-m1", "name": "Triplet Sum Close to Target", "url": "https://leetcode.com/problems/3sum-closest/"},
            {"id": "w0-m2", "name": "Triplets with Smaller Sum", "url": "https://leetcode.com/problems/3sum-smaller/"},
            {"id": "w0-m3", "name": "Subarrays with Product Less than a Target", "url": "https://leetcode.com/problems/subarray-product-less-than-k/"},
            {"id": "w0-m4", "name": "Dutch National Flag Problem", "url": "https://leetcode.com/problems/sort-colors/"},
            {"id": "w0-m5", "name": "Quadruple Sum to Target", "url": "https://leetcode.com/problems/4sum/"},
            {"id": "w0-m6", "name": "Comparing Strings containing Backspaces", "url": "https://leetcode.com/problems/backspace-string-compare/"},
            {"id": "w0-m7", "name": "Minimum Window Sort", "url": "https://leetcode.com/problems/shortest-unsorted-continuous-subarray/"},
            {"id": "w0-m8", "name": "Start of LinkedList Cycle", "url": "https://leetcode.com/problems/linked-list-cycle-ii/"},
            {"id": "w0-m9", "name": "Happy Number", "url": "https://leetcode.com/problems/happy-number/"},
            {"id": "w0-m10", "name": "Palindrome LinkedList", "url": "https://leetcode.com/problems/palindrome-linked-list/"},
            {"id": "w0-m11", "name": "Rearrange a LinkedList", "url": "https://leetcode.com/problems/odd-even-linked-list/"},
        ],
        "hard": [
            {"id": "w0-h0", "name": "Cycle in a Circular Array", "url": "https://leetcode.com/problems/circular-array-loop/"},
        ],
    },
    {
        "week": "Sliding Window and Merge Intervals",
        "easy": [
            {"id": "w1-e0", "name": "Maximum Sum Subarray of Size K", "url": "https://leetcode.com/problems/maximum-average-subarray-i/"},
            {"id": "w1-e1", "name": "Smallest Subarray with a Given Sum", "url": "https://leetcode.com/problems/minimum-size-subarray-sum/"},
        ],
        "medium": [
            {"id": "w1-m0", "name": "Longest Substring with K Distinct Characters", "url": "https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/"},
            {"id": "w1-m1", "name": "Fruits into Baskets", "url": "https://leetcode.com/problems/fruit-into-baskets/"},
            {"id": "w1-m2", "name": "Merge Intervals", "url": "https://leetcode.com/problems/merge-intervals/"},
            {"id": "w1-m3", "name": "Insert Interval", "url": "https://leetcode.com/problems/insert-interval/"},
            {"id": "w1-m4", "name": "Intervals Intersection", "url": "https://leetcode.com/problems/interval-list-intersections/"},
            {"id": "w1-m5", "name": "Conflicting Appointments", "url": "https://leetcode.com/problems/meeting-rooms/"},
        ],
        "hard": [
            {"id": "w1-h0", "name": "No-repeat Substring", "url": "https://leetcode.com/problems/longest-substring-without-repeating-characters/"},
            {"id": "w1-h1", "name": "Longest Substring with Same Letters after Replacement", "url": "https://leetcode.com/problems/longest-repeating-character-replacement/"},
            {"id": "w1-h2", "name": "Longest Subarray with Ones after Replacement", "url": "https://leetcode.com/problems/max-consecutive-ones-iii/"},
            {"id": "w1-h3", "name": "Permutation in a String", "url": "https://leetcode.com/problems/permutation-in-string/"},
            {"id": "w1-h4", "name": "String Anagrams", "url": "https://leetcode.com/problems/find-all-anagrams-in-a-string/"},
            {"id": "w1-h5", "name": "Smallest Window containing Substring", "url": "https://leetcode.com/problems/minimum-window-substring/"},
            {"id": "w1-h6", "name": "Words Concatenation", "url": "https://leetcode.com/problems/substring-with-concatenation-of-all-words/"},
            {"id": "w1-h7", "name": "Minimum Meeting Rooms", "url": "https://leetcode.com/problems/meeting-rooms-ii/"},
            {"id": "w1-h8", "name": "Maximum CPU Load", "url": "https://leetcode.com/problems/maximum-subarray/"},
            {"id": "w1-h9", "name": "Employee Free Time", "url": "https://leetcode.com/problems/employee-free-time/"},
        ],
    },
    {
        "week": "Cyclic Sort and In-place reversal of Linked List",
        "easy": [
            {"id": "w2-e0", "name": "Cyclic Sort", "url": "https://leetcode.com/problems/missing-number/"},
            {"id": "w2-e1", "name": "Find the Missing Number", "url": "https://leetcode.com/problems/missing-number/"},
            {"id": "w2-e2", "name": "Find all Missing Numbers", "url": "https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/"},
            {"id": "w2-e3", "name": "Find the Duplicate Number", "url": "https://leetcode.com/problems/find-the-duplicate-number/"},
            {"id": "w2-e4", "name": "Find all Duplicate Numbers", "url": "https://leetcode.com/problems/find-all-duplicates-in-an-array/"},
            {"id": "w2-e5", "name": "Find the Corrupt Pair", "url": "https://leetcode.com/problems/set-mismatch/"},
            {"id": "w2-e6", "name": "Reverse a LinkedList", "url": "https://leetcode.com/problems/reverse-linked-list/"},
        ],
        "medium": [
            {"id": "w2-m0", "name": "Find the Smallest Missing Positive Number", "url": "https://leetcode.com/problems/first-missing-positive/"},
            {"id": "w2-m1", "name": "Reverse a Sub-list", "url": "https://leetcode.com/problems/reverse-linked-list-ii/"},
            {"id": "w2-m2", "name": "Reverse every K-element Sub-list", "url": "https://leetcode.com/problems/reverse-nodes-in-k-group/"},
            {"id": "w2-m3", "name": "Reverse alternating K-element Sub-list", "url": "https://leetcode.com/problems/reverse-nodes-in-k-group/"},
            {"id": "w2-m4", "name": "Rotate a LinkedList", "url": "https://leetcode.com/problems/rotate-list/"},
        ],
        "hard": [
            {"id": "w2-h0", "name": "Find the First K Missing Positive Numbers", "url": "https://leetcode.com/problems/kth-missing-positive-number/"},
        ],
    },
    {
        "week": "Stack and Monotonic Stack",
        "easy": [
            {"id": "w3-e0", "name": "Balanced Parentheses", "url": "https://leetcode.com/problems/valid-parentheses/"},
            {"id": "w3-e1", "name": "Reverse a String", "url": "https://leetcode.com/problems/reverse-string/"},
            {"id": "w3-e2", "name": "Remove All Adjacent Duplicates In String", "url": "https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/"},
            {"id": "w3-e3", "name": "Next Greater Element I", "url": "https://leetcode.com/problems/next-greater-element-i/"},
            {"id": "w3-e4", "name": "Daily Temperatures", "url": "https://leetcode.com/problems/daily-temperatures/"},
            {"id": "w3-e5", "name": "Remove Nodes From Linked List", "url": "https://leetcode.com/problems/remove-nodes-from-linked-list/"},
        ],
        "medium": [
            {"id": "w3-m0", "name": "Decimal to Binary Conversion", "url": "https://leetcode.com/problems/convert-a-number-to-hexadecimal/"},
            {"id": "w3-m1", "name": "Next Greater Element II", "url": "https://leetcode.com/problems/next-greater-element-ii/"},
            {"id": "w3-m2", "name": "Simplify Path", "url": "https://leetcode.com/problems/simplify-path/"},
            {"id": "w3-m3", "name": "Remove All Adjacent Duplicates in String II", "url": "https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/"},
        ],
        "hard": [
            {"id": "w3-h0", "name": "Next Greater Element III", "url": "https://leetcode.com/problems/next-greater-element-iii/"},
            {"id": "w3-h1", "name": "Sorting a Stack", "url": "https://leetcode.com/problems/sort-an-array/"},
            {"id": "w3-h2", "name": "Remove K Digits", "url": "https://leetcode.com/problems/remove-k-digits/"},
        ],
    },
    {
        "week": "Hash Maps and Tree : BFS",
        "easy": [
            {"id": "w4-e0", "name": "First Non-repeating Character", "url": "https://leetcode.com/problems/first-unique-character-in-a-string/"},
            {"id": "w4-e1", "name": "Largest Unique Number", "url": "https://leetcode.com/problems/largest-unique-number/"},
            {"id": "w4-e2", "name": "Maximum Number of Balloons", "url": "https://leetcode.com/problems/maximum-number-of-balloons/"},
            {"id": "w4-e3", "name": "Longest Palindrome", "url": "https://leetcode.com/problems/longest-palindrome/"},
            {"id": "w4-e4", "name": "Ransom Note", "url": "https://leetcode.com/problems/ransom-note/"},
            {"id": "w4-e5", "name": "Binary Tree Level Order Traversal", "url": "https://leetcode.com/problems/binary-tree-level-order-traversal/"},
            {"id": "w4-e6", "name": "Reverse Level Order Traversal", "url": "https://leetcode.com/problems/binary-tree-level-order-traversal/"},
            {"id": "w4-e7", "name": "Level Averages in a Binary Tree", "url": "https://leetcode.com/problems/average-of-levels-in-binary-tree/"},
            {"id": "w4-e8", "name": "Minimum Depth of a Binary Tree", "url": "https://leetcode.com/problems/minimum-depth-of-binary-tree/"},
            {"id": "w4-e9", "name": "Maximum Depth of a Binary Tree", "url": "https://leetcode.com/problems/maximum-depth-of-binary-tree/"},
            {"id": "w4-e10", "name": "Level Order Successor", "url": "https://www.geeksforgeeks.org/level-order-successor-of-a-given-node-in-binary-tree/"},
            {"id": "w4-e11", "name": "Right View of a Binary Tree", "url": "https://leetcode.com/problems/binary-tree-right-side-view/"},
        ],
        "medium": [
            {"id": "w4-m0", "name": "Zigzag Traversal", "url": "https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/"},
            {"id": "w4-m1", "name": "Connect Level Order Siblings", "url": "https://leetcode.com/problems/populating-next-right-pointers-in-each-node/"},
            {"id": "w4-m2", "name": "Connect All Level Order Siblings", "url": "https://www.educative.io/courses/grokking-the-coding-interview/7n3bl"},
        ],
        "hard": []
    },
    {
        "week": "Tree : DFS and Graph",
        "easy": [
            {"id": "w5-e0", "name": "Binary Tree Path Sum", "url": "https://leetcode.com/problems/path-sum/"},
            {"id": "w5-e1", "name": "Find if Path Exists in Graph", "url": "https://leetcode.com/problems/find-if-path-exists-in-graph/"},
        ],
        "medium": [
            {"id": "w5-m0", "name": "All Paths for a Sum", "url": "https://leetcode.com/problems/path-sum-ii/"},
            {"id": "w5-m1", "name": "Sum of Path Numbers", "url": "https://leetcode.com/problems/sum-root-to-leaf-numbers/"},
            {"id": "w5-m2", "name": "Path With Given Sequence", "url": "https://www.geeksforgeeks.org/check-if-a-given-array-can-represent-preorder-traversal-of-binary-search-tree/"},
            {"id": "w5-m3", "name": "Count Paths for a Sum", "url": "https://leetcode.com/problems/path-sum-iii/"},
            {"id": "w5-m4", "name": "Tree Diameter", "url": "https://leetcode.com/problems/diameter-of-binary-tree/"},
            {"id": "w5-m5", "name": "Number of Provinces", "url": "https://leetcode.com/problems/number-of-provinces/"},
            {"id": "w5-m6", "name": "Minimum Number of Vertices to Reach All Nodes", "url": "https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/"},
        ],
        "hard": [
            {"id": "w5-h0", "name": "Path with Maximum Sum", "url": "https://leetcode.com/problems/binary-tree-maximum-path-sum/"},
        ],
    },
    {
        "week": "Island and Two Heaps",
        "easy": [
            {"id": "w6-e0", "name": "Number of Islands", "url": "https://leetcode.com/problems/number-of-islands/"},
            {"id": "w6-e1", "name": "Biggest Island", "url": "https://leetcode.com/problems/making-a-large-island/"},
            {"id": "w6-e2", "name": "Flood Fill", "url": "https://leetcode.com/problems/flood-fill/"},
            {"id": "w6-e3", "name": "Number of Closed Islands", "url": "https://leetcode.com/problems/number-of-closed-islands/"},
        ],
        "medium": [
            {"id": "w6-m0", "name": "Find the Median of a Number Stream", "url": "https://leetcode.com/problems/find-median-from-data-stream/"},
            {"id": "w6-m1", "name": "Maximum Sum Combinations", "url": "https://leetcode.com/problems/find-k-pairs-with-smallest-sums/"},
        ],
        "hard": [
            {"id": "w6-h0", "name": "Sliding Window Median", "url": "https://leetcode.com/problems/sliding-window-median/"},
            {"id": "w6-h1", "name": "Maximize Capital", "url": "https://leetcode.com/problems/ipo/"},
        ],
    },
    {
        "week": "Subsets and Modified Binary Search",
        "easy": [
            {"id": "w7-e0", "name": "Subsets", "url": "https://leetcode.com/problems/subsets/"},
            {"id": "w7-e1", "name": "Subsets With Duplicates", "url": "https://leetcode.com/problems/subsets-ii/"},
            {"id": "w7-e2", "name": "Order-agnostic Binary Search", "url": "https://leetcode.com/problems/search-in-rotated-sorted-array/"},
            {"id": "w7-e3", "name": "Bitonic Array Maximum", "url": "https://leetcode.com/problems/peak-index-in-a-mountain-array/"},
        ],
        "medium": [
            {"id": "w7-m0", "name": "Permutations", "url": "https://leetcode.com/problems/permutations/"},
            {"id": "w7-m1", "name": "Ceiling of a Number", "url": "https://leetcode.com/problems/find-smallest-letter-greater-than-target/"},
            {"id": "w7-m2", "name": "Next Letter", "url": "https://leetcode.com/problems/find-smallest-letter-greater-than-target/"},
            {"id": "w7-m3", "name": "Number Range", "url": "https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/"},
            {"id": "w7-m4", "name": "Search in a Sorted Infinite Array", "url": "https://leetcode.com/problems/search-in-rotated-sorted-array/"},
            {"id": "w7-m5", "name": "Minimum Difference Element", "url": "https://leetcode.com/problems/minimum-absolute-difference/"},
            {"id": "w7-m6", "name": "Search Bitonic Array", "url": "https://leetcode.com/problems/find-in-mountain-array/"},
            {"id": "w7-m7", "name": "Search in Rotated Array", "url": "https://leetcode.com/problems/search-in-rotated-sorted-array/"},
            {"id": "w7-m8", "name": "Rotation Count", "url": "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/"},
            {"id": "w7-m9", "name": "Search a 2D Matrix", "url": "https://leetcode.com/problems/search-a-2d-matrix/"},
            {"id": "w7-m10", "name": "Minimum Number of Days to Make m Bouquets", "url": "https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/"},
            {"id": "w7-m11", "name": "Koko Eating Bananas", "url": "https://leetcode.com/problems/koko-eating-bananas/"},
            {"id": "w7-m12", "name": "Capacity To Ship Packages Within D Days", "url": "https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/"},
        ],
        "hard": [
            {"id": "w7-h0", "name": "Median of Two Sorted Arrays", "url": "https://leetcode.com/problems/median-of-two-sorted-arrays/"},
        ],
    },
    {
        "week": "Bitwise XOR and Top K Elements",
        "easy": [
            {"id": "w8-e0", "name": "Single Number", "url": "https://leetcode.com/problems/single-number/"},
            {"id": "w8-e1", "name": "Top 'K' Numbers", "url": "https://leetcode.com/problems/top-k-frequent-elements/"},
            {"id": "w8-e2", "name": "Kth Smallest Number", "url": "https://leetcode.com/problems/kth-smallest-element-in-a-bst/"},
            {"id": "w8-e3", "name": "'K' Closest Points to the Origin", "url": "https://leetcode.com/problems/k-closest-points-to-origin/"},
            {"id": "w8-e4", "name": "Connect Ropes", "url": "https://leetcode.com/problems/minimum-cost-to-connect-sticks/"},
        ],
        "medium": [
            {"id": "w8-m0", "name": "Two Single Numbers", "url": "https://leetcode.com/problems/single-number-iii/"},
            {"id": "w8-m1", "name": "Complement of Base 10 Number", "url": "https://leetcode.com/problems/complement-of-base-10-integer/"},
            {"id": "w8-m2", "name": "Top 'K' Frequent Numbers", "url": "https://leetcode.com/problems/top-k-frequent-elements/"},
            {"id": "w8-m3", "name": "Frequency Sort", "url": "https://leetcode.com/problems/sort-characters-by-frequency/"},
            {"id": "w8-m4", "name": "Kth Largest Number in a Stream", "url": "https://leetcode.com/problems/kth-largest-element-in-a-stream/"},
        ],
        "hard": [
            {"id": "w8-h0", "name": "Flip and Invert an Image", "url": "https://leetcode.com/problems/flipping-an-image/"},
        ],
    },
    {
        "week": "K-way merge and Greedy Sort",
        "easy": [
            {"id": "w9-e0", "name": "Valid Palindrome II", "url": "https://leetcode.com/problems/valid-palindrome-ii/"},
        ],
        "medium": [
            {"id": "w9-m0", "name": "Merge K Sorted Lists", "url": "https://leetcode.com/problems/merge-k-sorted-lists/"},
            {"id": "w9-m1", "name": "Kth Smallest Number in M Sorted Lists", "url": "https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/"},
            {"id": "w9-m2", "name": "Maximum Length of Pair Chain", "url": "https://leetcode.com/problems/maximum-length-of-pair-chain/"},
            {"id": "w9-m3", "name": "Minimum Add to Make Parentheses Valid", "url": "https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/"},
            {"id": "w9-m4", "name": "Remove Duplicate Letters", "url": "https://leetcode.com/problems/remove-duplicate-letters/"},
            {"id": "w9-m5", "name": "Removing Minimum and Maximum From Array", "url": "https://leetcode.com/problems/removing-minimum-and-maximum-from-array/"},
            {"id": "w9-m6", "name": "Largest Palindromic Number", "url": "https://leetcode.com/problems/largest-palindromic-number/"},
        ],
        "hard": [
            {"id": "w9-h0", "name": "Kth Smallest Number in a Sorted Matrix", "url": "https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/"},
            {"id": "w9-h1", "name": "Smallest Number Range", "url": "https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/"},
        ],
    },
    {
        "week": "0/1 Knapsack and BackTracking",
        "easy": [],
        "medium": [
            {"id": "w10-m0", "name": "0/1 Knapsack", "url": "https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/"},
            {"id": "w10-m1", "name": "Equal Subset Sum Partition", "url": "https://leetcode.com/problems/partition-equal-subset-sum/"},
            {"id": "w10-m2", "name": "Subset Sum", "url": "https://leetcode.com/problems/target-sum/"},
            {"id": "w10-m3", "name": "Combination Sum I", "url": "https://leetcode.com/problems/combination-sum/"},
            {"id": "w10-m4", "name": "Combination Sum II", "url": "https://leetcode.com/problems/combination-sum-ii/"},
            {"id": "w10-m5", "name": "Combination Sum III", "url": "https://leetcode.com/problems/combination-sum-iii/"},
            {"id": "w10-m6", "name": "Combination Sum IV", "url": "https://leetcode.com/problems/combination-sum-iv/"},
            {"id": "w10-m7", "name": "Word Search I", "url": "https://leetcode.com/problems/word-search/"},
            {"id": "w10-m8", "name": "Factor Combinations", "url": "https://leetcode.com/problems/factor-combinations/"},
            {"id": "w10-m9", "name": "Split a String Into the Max Number of Unique Substrings", "url": "https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/"},
        ],
        "hard": [
            {"id": "w10-h0", "name": "Minimum Subset Sum Difference", "url": "https://leetcode.com/problems/last-stone-weight-ii/"},
            {"id": "w10-h1", "name": "Word Search II", "url": "https://leetcode.com/problems/word-search-ii/"},
            {"id": "w10-h2", "name": "Sudoku Solver", "url": "https://leetcode.com/problems/sudoku-solver/"},
        ],
    },
    {
        "week": "Trie and Topological Sort",
        "easy": [
            {"id": "w11-e0", "name": "Index Pairs of a String", "url": "https://leetcode.com/problems/index-pairs-of-a-string/"},
        ],
        "medium": [
            {"id": "w11-m0", "name": "Implement Trie (Prefix Tree)", "url": "https://leetcode.com/problems/implement-trie-prefix-tree/"},
            {"id": "w11-m1", "name": "Design Add and Search Words Data Structure", "url": "https://leetcode.com/problems/add-and-search-word-data-structure-design/"},
            {"id": "w11-m2", "name": "Extra Characters in a String", "url": "https://leetcode.com/problems/extra-characters-in-a-string/"},
            {"id": "w11-m3", "name": "Search Suggestions System", "url": "https://leetcode.com/problems/search-suggestions-system/"},
            {"id": "w11-m4", "name": "Topological Sort", "url": "https://www.youtube.com/watch?v=ddTC4Zovtbc"},
            {"id": "w11-m5", "name": "Tasks Scheduling", "url": "https://leetcode.com/problems/course-schedule/"},
            {"id": "w11-m6", "name": "Tasks Scheduling Order", "url": "https://leetcode.com/problems/course-schedule-ii/"},
        ],
        "hard": [
            {"id": "w11-h0", "name": "All Tasks Scheduling Orders", "url": "https://leetcode.com/problems/parallel-courses-iii/"},
            {"id": "w11-h1", "name": "Alien Dictionary", "url": "https://leetcode.com/problems/alien-dictionary/"},
            {"id": "w11-h2", "name": "Reconstructing a Sequence", "url": "https://leetcode.com/problems/sequence-reconstruction/"},
            {"id": "w11-h3", "name": "Minimum Height Trees", "url": "https://leetcode.com/problems/minimum-height-trees/"},
        ],
    },
    {
        "week": "Union Find , Ordered Set and Multi-thread",
        "easy": [
            {"id": "w12-e0", "name": "Merge Similar Items", "url": "https://leetcode.com/problems/merge-similar-items/"},
        ],
        "medium": [
            {"id": "w12-m0", "name": "Redundant Connection I", "url": "https://leetcode.com/problems/redundant-connection/"},
            {"id": "w12-m1", "name": "Number of Provinces", "url": "https://leetcode.com/problems/number-of-provinces/"},
            {"id": "w12-m2", "name": "Is Graph Bipartite?", "url": "https://leetcode.com/problems/is-graph-bipartite/"},
            {"id": "w12-m3", "name": "Path With Minimum Effort", "url": "https://leetcode.com/problems/path-with-minimum-effort/"},
            {"id": "w12-m4", "name": "132 Pattern", "url": "https://leetcode.com/problems/132-pattern/"},
            {"id": "w12-m5", "name": "My Calendar I", "url": "https://leetcode.com/problems/my-calendar-i/"},
        ],
        "hard": [
            {"id": "w12-h0", "name": "Redundant Connection II", "url": "https://leetcode.com/problems/redundant-connection-ii/"},
            {"id": "w12-h1", "name": "My Calendar II", "url": "https://leetcode.com/problems/my-calendar-ii/"},
            {"id": "w12-h2", "name": "My Calendar III", "url": "https://leetcode.com/problems/my-calendar-iii/"},
        ],
    },
]


# --- SIDEBAR NAVIGATION ---
st.sidebar.markdown("# 🧭 Navigate")
page = st.sidebar.radio("", ["Dashboard", "This Week", "Full Plan", "Settings"])
st.sidebar.markdown("---")
st.sidebar.markdown("**Tip:** _" + random.choice([
    "Code like it's poetry.",
    "Every problem is an opportunity.",
    "Push your limits! 🌟"
]) + "_")

# --- DASHBOARD ---
if page == "Dashboard":
    st.title("🏠 Dashboard")
    col1, col2, col3 = st.columns(3)
    col1.metric("🔥 Streak", f"{state['streak']} days")
    col2.metric("✅ Solved", len(state['completed']))
    current_week = 1 + len(state['completed']) // 10
    col3.metric("📅 Week", f"{current_week}/14")
    st.markdown("---")
    st.subheader("Progress Heatmap 🔥")
    st.write("(Heatmap)")
    st.markdown("---")

# --- THIS WEEK ---
elif page == "This Week":
    st.title("🎯 Week-by-Week Practice")
    # compute default
    default_week = 1 + len(state["completed"]) // 10
    # slider you can arrow through
    week_num = st.sidebar.select_slider(
        "Jump to Week",
        options=list(range(1, len(JOURNEY) + 1)),
        value=default_week,
        format_func=lambda x: f"Week {x}"
    )
    week_idx = week_num - 1
    week = JOURNEY[week_idx]

    st.subheader(f"Week {week_num}: {week['week']}")
    for level in ["easy", "medium", "hard"]:
        st.markdown(f"**{level.capitalize()}**")
        for prob in week[level]:
            cols = st.columns([0.8, 0.2])
            cols[0].markdown(f"- [{prob['name']}]({prob['url']})")
            done = prob["id"] in state["completed"]
            cb = cols[1].checkbox("Done", value=done, key=prob["id"])
            if cb and not done:
                state["completed"].append(prob["id"])
                save_state(state)
            elif not cb and done:
                state["completed"].remove(prob["id"])
                save_state(state)

# --- FULL PLAN ---
elif page == "Full Plan":
    st.title("🗺️ Full 14-Week Plan")
    for i, w in enumerate(JOURNEY):
        exp = st.expander(f"Week {i+1}: {w['week']}", expanded=False)
        with exp:
            for lvl in ["easy", "medium", "hard"]:
                st.markdown(f"**{lvl.capitalize()}**")
                for prob in w[lvl]:
                    status = "✅" if prob["id"] in state["completed"] else "❌"
                    st.markdown(f"- {status} [{prob['name']}]({prob['url']})")

# --- SETTINGS ---
elif page == "Settings":
    st.title("⚙️ Settings")
    theme = st.selectbox("Theme", ["Dark", "Light"], index=0)
    if st.button("Reset Progress"):
        st.session_state.state = init_state()
        save_state(st.session_state.state)
        st.experimental_rerun()

# --- FOOTER ---
st.markdown("---")
st.markdown("*Built for 2025. Keep coding! 🚀*")
