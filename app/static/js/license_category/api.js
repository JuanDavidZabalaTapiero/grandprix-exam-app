export async function getCategories() {
  const response = await fetch("/api/license-categories/");
  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.message);
  }

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
