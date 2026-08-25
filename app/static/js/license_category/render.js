import { icons } from "../icons.js";
import { handleDeleteCategory } from "./controller.js";

export function renderCategories(container, categories) {
  container.innerHTML = "";

  if (categories.length === 0) {
    container.textContent = "No hay categorías registradas.";
    return;
  }

  // dataset
  const updateUrl = container.dataset.updateUrl;

  categories.forEach((category) => {
    const element = document.createElement("div");
    element.textContent = category.name;
    element.classList.add("element");

    const div = document.createElement("div");
    div.classList.add("actions");

    // edit
    const link = document.createElement("a");
    link.href = updateUrl.replace("0", category.id);
    link.innerHTML = icons.pencil;
    link.classList.add("edit-btn");

    // delete
    const button = document.createElement("button");
    button.innerHTML = icons.trash;
    button.classList.add("delete-btn");

    button.addEventListener("click", () => {
      handleDeleteCategory(category.id);
    });
    div.appendChild(link);
    div.appendChild(button);
    element.appendChild(div);
    container.appendChild(element);
  });
}
