export function showMessage(message, category) {
  const container = document.getElementById("messages");

  const messageElement = document.createElement("div");
  messageElement.classList.add("message");
  messageElement.classList.add(category);
  messageElement.textContent = message;

  container.appendChild(messageElement);
}
