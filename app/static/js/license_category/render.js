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

    // edit
    const link = document.createElement("a");
    link.href = updateUrl.replace("0", category.id);
    link.innerHTML = icons.pencil;

    // delete
    const button = document.createElement("button");
    button.innerHTML = icons.trash;

    button.addEventListener("click", () => {
      handleDeleteCategory(category.id);
    });

    element.appendChild(link);
    element.appendChild(button);
    container.appendChild(element);
  });
}
