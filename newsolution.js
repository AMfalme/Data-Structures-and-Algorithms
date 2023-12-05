// Input: [2,2,2]
//  Output: [2,3,4] = (3)


function solution1(params) {
    var counts = 0;
    for (var i = 1; i < params.length; i++){
        while(params[i] <= params[i-1]){
            params[i] += 1
            counts += 1
        }
    }
    return counts
}



function solution2(args) {
    var divisibles = 0;
    for (let value of args.toString()) {
        if (args % parseInt(value) == 0) {
            divisibles += 1 
        }
    }
    return divisibles
}

// console.log(solution1([2,2,2]))
// console.log(solution1([4,4,7]))


console.log(solution2(232))

