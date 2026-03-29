const headerElement = document.querySelector('header');
const redHeaderButton = document.querySelector('#red_header');

redHeaderButton.addEventListener('click', function() {
  headerElement.style.color = '#FF0000';
});
