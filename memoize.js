// class Memoize {
//     constructor(fn, size){
//         const res = {};
//     }
//     getResult() {

//     }


//     createResult() {

//     }
// }

function MemoizeClumsy(fn, context) {
    const res = {}
    return function(...args) {
        var argsCache = JSON.stringify(args);
        if (!res[argsCache]) {
            res[argsCache] = fn.call(context || this, ...args)
        }

        return res[argsCache]

    }
}


function clumsy(nums, nums2) {
    for (let i = 0; i < 1000000000; i++) {}

    return nums* nums2;
}


const memoizedProduct = MemoizeClumsy(clumsy)

console.time('First call ')
console.log(memoizedProduct(9456, 7649));
console.timeEnd('First call ')


console.time('Second call ')
console.log(memoizedProduct(9456, 7649));
console.timeEnd('Second call ')



// Impliment currying below

console.log(add(5)(2)(4)(5)());

function add(a) {

    return function (b) {
        if (b) {
            return add(a+b)
     
        } return a
    }
}