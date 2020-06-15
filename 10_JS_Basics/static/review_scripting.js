// Want to talk about some of the most basic variables of javascript


var stringer = "This is a JS string";

var num_val = 90;

var text_num = "102";

var parsed_num = parseInt(text_num);

var boolean = true;

var boolean2 = false;



/*Although one can make the argument that JS has a lot fewer in-built functions than vanilla 
Python, there is still a lot that you can do with math! */
var new_num = 10.501

//rounding
Math.round(new_num)

//absolute value
Math.abs(-new_num)

//exponents
Math.pow(new_num, 2)

//random number generator
Math.random()



/* It is always a good habit to fall into to print variables to your console when you're debugging.
I always end up doing a similar thing in whatever language I'm working in whether it's Python or JS.
NOTE: This is also how you do a multiline comment! */

console.log(boolean == boolean2);

console.log(boolean === true);

console.log(`${stringer}`);

console.log(`${boolean} is not equal to ${boolean2}`);



/* The next thing that I'll want to review here is going to be some boolean logic which is
important in both JS and Python. I want to also take a moment to talk about how the structure
of javascript works (note, there is none)*/

if (num_val==90){console.log("This is the same as the statement below");}else{console.log("This is still the same as the statement below")};


if (num_val==90) {
	console.log("This is the same as the statement above");
}
else {
	console.log("This is still the same as the statement above");
};



/*Want to take a moment to briefly talk about if/elseif/else statements in javascript, and then will
also pack up a function to check for grades
https://www.w3schools.com/js/js_switch.asp*/

var grade_val = 92;

function grader(grade_val){
  if (grade_val === 105) {
    console.log(`A grade of ${grade_val} is the best grade ever!`);
  }
else if (grade_val >= 90) {
    console.log(`A grade of ${grade_val} is an A!`);
  }
  else if (grade_val >= 80) {
    console.log(`A grade of ${grade_val} is an B!`);
  }
  else if (grade_val >= 70) {
    console.log(`A grade of ${grade_val} is an C!`);
  }
  else if (grade_val >= 60) {
    console.log(`A grade of ${grade_val} is an D!`);
  }
  else {
    console.log(`A grade of ${grade_val} is an F!`);
  }};



 //Next we're going to just take a quick look at how loops are formed in javascript
var final_var = 0

for(var i = 0; i < 50; i++)
{
	final_var = final_var+=i 
}



//Want to also consider what would happen if we were to add a break statement to this loop.
for (var i = 0; i < 50; i++)
{
    if (i == 20) { break;}         
    console.log(i);
}



//We can also use a for loop to iterate through a list in javascript.*/

function print_stufflist(){
var stuff_list = ['pan', 'desk', 'cup', 'can'];

for(var i = 0; i < stuff_list.length; i++)
	{console.log(`${stuff_list[i]} is an item in the house`)}
}



/* Another really important part of Javascript (and Python as well) is the JSON object which functions a lot like a Python dictionary.  */
var scope_stuff_json = {
	first_item : "pan",
	second_item : "desk",
	third_item : "cup",
	fourth_item : "can"
};

function json_exposition(){
var stuff_json = {
	first_item : "pan",
	second_item : "desk",
	third_item : "cup",
	fourth_item : "can"
};

console.log(stuff_json);

console.log(Object.keys(stuff_json));

console.log(Object.values(stuff_json));
};



/*Now we'll want to do some array manipulations*/

//creating it
working_array = ['this', 'is', 'an', 'array'];

//output as a string
working_array.toString();

//removing 2 items from the array
working_array.pop();
working_array.shift();

//adding some items back into the array
working_array.push('array!');
working_array.unshift('that');
working_array.unshift('know');
working_array.unshift('We');

//Now we're going to create a new array and append it to the end of working_array.
second_array = ['this', 'is', 'another'];
working_array.concat(second_array);

/*some final in-built array manipulation like sorting and reverse sort (keep in mind
that lowercase and uppercase letters may be handled differently)*/

working_array.sort();
working_array.reverse();



//We'll want to keep in mind that we can 
function spam_console() {
	console.log('You clicked a button!')
}

//create a function to throw an error, note that we will have to click a button to invoke this.
function cause_error(){
	throw "You broke everything!"
}


//creating an anonymous function to do addition for us
var funky = function(first, second) {return first + second};




/*
https://news.codecademy.com/your-guide-to-semicolons-in-javascript/

https://www.educba.com/python-vs-javascript/

https://htmlcheatsheet.com/js/

I will say that I'm far from the best JS coder so the amount of lessons you can learn from the internet far outstrip what I can teach you, try to get in the habit of taking a look at different pages and seeing what functions are being called, that can always help. 
*/







