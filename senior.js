/*
You are given an object,
var John = {
    name: "John Doe",
    balance: 1500,
    deduct: function(amount) {
        this.balance -= amount
        return this.name+ " has a balance of " +this.balance
    }
}
1. use ES6, impliment ES6 features into the object. 
2. Return the value in 2 seconds

*/


// var John = {
//     name: "John Doe",
//     balance: 1500,
//     deduct: function(amount) {
//         this.balance -= amount
//         return this.name+ " has a balance of " +this.balance
//     }
// }

const John = {
    name: "John Doe",
    balance: 1500,
    deduct(amount) {
        this.balance -= amount
        return new Promise((res, rej)=> {
            setTimeout(() => {
                res(`${this.name} has a balance of ${this.balance}`)
            }, 2000 )
        })
        
    }
}


John.deduct(300).then(response => console.log(response));