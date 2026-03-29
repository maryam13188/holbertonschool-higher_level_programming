document.querySelector('#toggle_header').addEventListener('click', () => {
  const header = document.querySelector('header');
  const currentClass = header.classList.contains('red') ? 'red' : 'green';
  const newClass = currentClass === 'red' ? 'green' : 'red';
  header.classList.replace(currentClass, newClass);
});
