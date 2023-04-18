// Get a reference to the form and the target paragraph element
const form = document.querySelector('#source');
const target = document.querySelector('#target');

// Attach an event listener to the form's submit event
form.addEventListener('submit', event => {
  // Prevent the default form submission behavior
  event.preventDefault();

  // Get the values of the first and last name fields
  const firstName = document.querySelector('input[name="firstname"]').value;
  const lastName = document.querySelector('input[name="lastname"]').value;

  // Set the text content of the target paragraph element
  target.textContent = `Your name is ${firstName} ${lastName}`;
});
