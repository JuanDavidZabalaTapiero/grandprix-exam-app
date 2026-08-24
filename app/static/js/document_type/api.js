export async function getDocumentTypes() {
  const response = await fetch("/api/document-types");
  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.message);
  }

  return data.document_types;
}

export async function deleteDocumentType(documentTypeId) {
  const response = await fetch(`/api/document-types/${documentTypeId}`, {
    method: "DELETE",
  });
  const data = response.json();

  if (!response.ok) {
    throw new Error(data.message);
  }

  return data;
}
