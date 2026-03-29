document.querySelector('#add_item').addEventListener('click', () => {
  const myList = document.querySelector('.my_list');
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  myList.appendChild(newItem);
});
