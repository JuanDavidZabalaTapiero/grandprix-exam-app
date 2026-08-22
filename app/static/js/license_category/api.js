export async function getCategories() {
  const response = await fetch("/api/license-categories/");

  if (!response.ok) {
    throw new Error("Ocurrió un error al consultar las categorías.");
  }

  const data = await response.json();

  return data.categories;
}

export async function deleteCategory(categoryId) {
  const response = await fetch(`/api/license-categories/${categoryId}`, {
    method: "DELETE",
  });

  const data = response.json();

  if (!response.ok) {
    throw new Error(data.message);
  }

  return data;
}
