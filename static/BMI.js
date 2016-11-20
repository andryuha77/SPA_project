//    Adapted from: http://blog.excelstrategiesllc.com/2014/11/18/coding-your-first-javascript-bmi-calculator

/* BMI Calculator function*/
function BMICalculate()

/* Accept input variables*/
{
    var weight = document.getElementById('weight').value;
    var heightft = document.getElementById('heightft').value;

    /* Error Handling  for invalid data entered*/
    if (weight == "") {
        alert("Please enter your weight.");
        return;
    }
    if (heightft == "") {
        alert("Please enter your height.");
        return;
    }
    if (weight < 0) {
        alert("Your weight can only be negative in Theoretical Physics..., NOT in real life.");
        return;
    }
    if (weight < 30) {
        alert("Weighing " + weight + " lbs, you must be a child, this is Adult BMI calculator!");
        return;
    }
    if (weight > 1500) {
        alert("Do you really weigh " + weight + " pounds?!");
        return;
    }
    if (heightft < 0) {
        alert("Your can not possibly have a negative height!");
        return;
    }
    if (heightft < 3) {
        alert("Standing " + heightft + " feet tall, you must be a child, this is Adult BMI calculator!");
        return;
    }
    if (heightft > 10) {
        alert("Are you really " + heightft + " feet tall?!");
        return;
    }

    /* Performing calculations */
    var heightin = document.getElementById('heightin').value;
    var height = heightft * 12 + +heightin;

    BMI.innerHTML = Math.round((weight / (height * height)) * 703.06957964);
    getDescription(BMI.innerHTML);
}

/* Interpretation of BMI value */
function getDescription(thisBMI)
{
    var Description = "";
    if (thisBMI < 18.5)
        Description = "Underweight - eat a bagel!";
    else if (thisBMI >= 18.5 && thisBMI <= 24.99)
        Description = "Normal - keep it up!";
    else if (thisBMI >= 25 && thisBMI <= 29.99)
        Description = "Overweight - exercise more!";
    else if (thisBMI >= 30 && thisBMI <= 39.99)
        Description = "Obese - get off the couch!";
    else if (thisBMI >= 40)
        Description = "Morbidly Obese - take action!";
    else Description = "Please check your input values, BMI cannot be calculated.";

    var DESC = document.getElementById('DESC');
    document.cookie = Description;
}

/* Reset Button */
function Clear() {
    document.getElementById('weight').value = "";
    document.getElementById('heightft').value = "";
    document.getElementById('heightin').value = "";
    BMI.innerHTML = "";
}
