let number = 7;
let result;

switch (number % 2) {
  case 0:
    result = "Even";
    break;
  case 1:
    result = "Odd";
    break;
  default:
    result = "Invalid";
}

console.log("The number " + number + " is " + result);
