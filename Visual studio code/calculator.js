var application = require('./calc_functions.js');
console.log(application);
var a=10 , b=5;
console.log('a: '+a+' b: '+b);
 
console.log("Addition : "+application.add(a,b));
console.log("Subtraction : "+application.subtract(a,b));
console.log("Multiplication : "+application.multiply(a,b));
console.log("Division "+application.divide(a,b));