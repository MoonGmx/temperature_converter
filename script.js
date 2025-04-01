function convertTemp() {
    let value = document.getElementById('tempValue').value;
    let unit = document.getElementById('unit').value;
    let result = document.getElementById('result');
    
    if (unit === "celsius") {
        result.innerHTML = Fahrenheit: ${(value * 9/5 + 32).toFixed(2)}, Kelvin: ${(parseFloat(value) + 273.15).toFixed(2)};
    } else if (unit === "fahrenheit") {
        result.innerHTML = Celsius: ${((value - 32) * 5/9).toFixed(2)}, Kelvin: ${(((value - 32) * 5/9) + 273.15).toFixed(2)};
    } else if (unit === "kelvin") {
        result.innerHTML = Celsius: ${(value - 273.15).toFixed(2)}, Fahrenheit: ${((value - 273.15) * 9/5 + 32).toFixed(2)};
    } else {
        result.innerHTML = "Invalid unit!";
    }
}
