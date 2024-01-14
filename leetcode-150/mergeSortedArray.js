/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    let i = 0;
    let j = 0;
    let k = 0;
    let res = [null*(m+n)]
    
    while (nums1[i] < nums2[j]){
        res[k] = nums1[i]
        i++;
        k++;
    }
    while (nums2[j]< nums1[i]){
        res[k] = nums2[j];
        j++;
        k++;
    }
    console.log(res)
};


console.log(merge([1,2,3,0,0,0],6,[2,5,6], 3
    ))