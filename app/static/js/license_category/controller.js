import { showMessage } from "../messages.js";
import { getCategories, deleteCategory } from "./api.js";
import { renderCategories } from "./render.js";

export async function loadCategories() {
  const container = document.getElementById("categories");

  try {
    const categories = await getCategories();
    renderCategories(container, categories);
  } catch (error) {
    showMessage(error.message, "danger");
  }
}

export async function handleDeleteCategory(categoryId) {
  try {
    const data = await deleteCategory(categoryId);

    showMessage(data.message, "success");

    await loadCategories();
  } catch (error) {
    showMessage(error.message, "danger");
  }
}
