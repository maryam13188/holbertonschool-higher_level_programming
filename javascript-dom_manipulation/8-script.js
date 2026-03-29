document.addEventListener('DOMContentLoaded', async function() {
  const response = await fetch("https://hellosalut.stefanbohacek.com/?lang=fr");
  const data = await response.json();
  document.getElementById("hello").textContent = data.hello;
});
