
function validateName() {

    var name = document.getElementById('exampleInputUsername1').value;

  
    if(name.length == 0) {
  
      producePrompt('First Name is required', 'name-error' , 'red')
      return false;
  
    }
  
    if (!name.match(/^[A-Za-z]+$/)) {
  
      producePrompt('Only Alphabets allowed','name-error', 'red');
      return false;
  
    }
 
  
    producePrompt('', 'name-error', 'green');
    return true;
  
  }
function validatelastname() {

    var name = document.getElementById('exampleInputlastname1').value;

  
    if(name.length == 0) {
  
      producePrompt('Last Name is required', 'lastname-error' , 'red')
      return false;
    }
    if (!name.match(/^[A-Za-z]+$/)) {
      producePrompt('Only Alphabets allowed','lastname-error', 'red');
      return false;
    }
    producePrompt('', 'lastname-error', 'green');
    return true;

}
function validatelastname() {

    var name = document.getElementById('exampleInputlastname1').value;

  
    if(name.length == 0) {
  
      producePrompt('Last Name is required', 'lastname-error' , 'red')
      return false;
    }
    if (!name.match(/^[A-Za-z]+$/)) {
      producePrompt('Only Alphabets allowed','lastname-error', 'red');
      return false;
    }
 
  
    producePrompt('', 'lastname-error', 'green');
    return true;
  
  }

  function validateEmail () {
  
    var email = document.getElementById('exampleInputEmail1').value;
  
    if(email.length == 0) {
  
      producePrompt('Email Required','email-error', 'red');
      return false;
  
    }
  
    if(!email.match(/^[A-Za-z\._\-[0-9]*[@][A-Za-z]*[\.][a-z]{2,4}$/)) {
  
      producePrompt('Invalid Email', 'email-error', 'red');
      return false;
  
    }
  
    producePrompt('', 'email-error', 'green');
    return true;
  
  }
  function validatePassword () {
  
    var password1 = document.getElementById('exampleInputPassword1').value;
    var password2 = document.getElementById('exampleInputConfirmPassword1').value;
  
    if(password1 != password2) {
  
      producePrompt("Password doesn't match",'match-error', 'red');
      return false;
  
    }
    else{
    producePrompt('','match-error', 'green');
    return true;
    }
    }
  function validatePassword1 () {
  
    var password1 = document.getElementById('exampleInputPassword1').value;
    
  
    if(password1.length < 8) {
  
      producePrompt("Minimum 8 characters",'password-error', 'red');
      return false;
  
    }
    else{
    producePrompt('','password-error', 'green');
    return true;
    }
    }

  function producePrompt(message, promptLocation, color) {
  
    document.getElementById(promptLocation).innerHTML = message;
    document.getElementById(promptLocation).style.color = color;
  
  
  }
