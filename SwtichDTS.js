let productType = "shirt";
let price;

switch (productType) {
  case "shirt":
    price = 20;
    break;
  case "pants":
    price = 30;
    break;
  case "shoes":
    price = 50;
    break;
  default:
    price = "Unknown";
}

console.log("The price of the " + productType + " is $" + price);
