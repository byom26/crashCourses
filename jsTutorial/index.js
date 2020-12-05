// 1. Ways to print in JavaScript
// console.log("Hello World!");
// alert("Hello Alerts!");
// document.write("This is to write a document!");

// 2. Javascript console API
// console.log("Hello World!", 4+6, "Another log");
// console.warn("This is a warning!");
// console.error("This is a error!");
// console.assert(4==6);

// 3. JavaScript variables
// What are variables? => Containers to store data values
/*
Multi
line
comment
*/
// var number1 = 34;
// var number2 = 56;
// console.log(number1 + number2);

// 4. Data types in JavaScript
// Strings
// var str1 = "This is a string";
// var str2 = "This is a another string";
// Numbers
// var num1 = 34;
// var num2 = 56;
// Objects
// var marks = {
//     sachin: 34,
//     nandu: 79,
//     byom: 50
// }
// Booleans
// var a = true;
// var b = false;
// var und = undefined; // Both are same i.e. undefined
// var und;
// var n = null;
/*
At a very high level, there are two types of data types in JS
1. Primitve data types: Undefiend, Null, Number, String, Boolean, Symbol
2. Reference data types: Arrays & Objects
*/
// var arr = [1,2,3,4,5];
// console.log(arr[4]);

// 5. Operators in JS
// + - * /

// 6. Functions
/*
function avg(a, b){
    return (a+b)/2;
}
c1 = avg(10,5);
console.log(c1);
*/

// if-else statements
/*
var age = 108;
if (age < 18){
    console.log('You are a kid!');
}
else if(age > 100){
    console.log('You are really too old!');
}
else{
    console.log('You are not a kid!');
}
*/

// Loops
/*
var arr = [1,2,3,4,5,6];
console.log(arr);
for(var i=0; i<arr.length; i++){
    console.log(arr[i]);
}
*/

// Another way of looping over arrays
/*
var arr = [1,2,3,4,5,6];
arr.forEach(function(element){
    console.log(element);
})
*/

let j=0; // Scope is limited to a block only where as var scope is universal
// const a= 0;
let arr = [1,2,3,4,5,6,7,8];
while(j<arr.length){
    console.log(arr[j]);
    j++;
}