#include <iostream>
#include <vector>
using namespace std;

// Exercise 8 — Backtracking: Generate All Subsets
// Big-O: Time O(2^n * n), Space O(n) call stack + O(2^n * n) to store all subsets.
// A set of N elements has exactly 2^N subsets (including the empty set).
//
// Pattern:
//   1. Choose   — include nums[idx] in current subset
//   2. Explore  — recurse to idx + 1
//   3. Unchoose — remove nums[idx] to restore state (ROLLBACK)
//   Repeat without including nums[idx], then recurse.

void generateSubsets(const vector<int>& nums, int idx,
                     vector<int>& current, vector<vector<int>>& result) {
    // Base case: processed all elements — record current subset
    if (idx == static_cast<int>(nums.size())) {
        result.push_back(current);
        return;
    }

    // Branch 1: INCLUDE nums[idx]
    current.push_back(nums[idx]);          // choose
    generateSubsets(nums, idx + 1, current, result);   // explore
    current.pop_back();                    // unchoose (rollback)

    // Branch 2: EXCLUDE nums[idx]
    generateSubsets(nums, idx + 1, current, result);   // explore without it
}

void printSubsets(const vector<vector<int>>& subsets) {
    cout << "Total subsets: " << subsets.size() << endl;
    for (const auto& subset : subsets) {
        cout << "{ ";
        for (int x : subset) cout << x << " ";
        cout << "}" << endl;
    }
}

int main() {
    cout << "--- Backtracking: All Subsets ---" << endl;

    cout << "\n[nums = {1, 2, 3}]" << endl;
    vector<int> nums1 = {1, 2, 3};
    vector<int> current1;
    vector<vector<int>> result1;
    generateSubsets(nums1, 0, current1, result1);
    printSubsets(result1);  // should produce 2^3 = 8 subsets

    cout << "\n[nums = {5, 10}]" << endl;
    vector<int> nums2 = {5, 10};
    vector<int> current2;
    vector<vector<int>> result2;
    generateSubsets(nums2, 0, current2, result2);
    printSubsets(result2);  // should produce 2^2 = 4 subsets

    cout << "\n[nums = {}]" << endl;
    vector<int> nums3 = {};
    vector<int> current3;
    vector<vector<int>> result3;
    generateSubsets(nums3, 0, current3, result3);
    printSubsets(result3);  // should produce 2^0 = 1 subset: { }

    return 0;
}
