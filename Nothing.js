example 1


function getRandom(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

console.log(getRandom(1, 10)); 


example 2

function celsiusToFahrenheit(celsius) {
    return (celsius * 9/5) + 32;
}

console.log(celsiusToFahrenheit(30));


example 3

function removeDuplicates(arr) {
    return arr.filter((value, index, self) => self.indexOf(value) === index);
}

console.log(removeDuplicates([1, 2, 2, 3, 4, 4, 5]));


example 4

function generateUUID() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        const r = Math.random() * 16 | 0, v = c === 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}


example 5

