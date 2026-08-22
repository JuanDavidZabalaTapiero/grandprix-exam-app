import { handleDeleteCategory } from "./controller.js";

const categoriesContainer = document.getElementById("categories");

export function renderCategories(categories) {
  categoriesContainer.innerHTML = "";

  if (categories.length === 0) {
    categoriesContainer.textContent = "No hay categorías registradas.";
  }

  const updateUrl = categoriesContainer.dataset.updateUrl;

  categories.forEach((category) => {
    const element = document.createElement("div");
    element.textContent = category.name;

    const link = document.createElement("a");
    link.href = updateUrl.replace("0", category.id);
    link.textContent = "EDIT";

    const button = document.createElement("button");
    button.textContent = "DELETE";

    // Evento
    button.addEventListener("click", () => {
      handleDeleteCategory(category.id);
    });

    element.appendChild(link);
    element.appendChild(button);
    categoriesContainer.appendChild(element);
  });
}
