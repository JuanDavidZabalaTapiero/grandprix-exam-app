import { showMessage } from "../messages.js";
import { getDocumentTypes, deleteDocumentType } from "./api.js";
import { renderDocumentTypes } from "./render.js";

export async function loadDocumentTypes() {
  const container = document.getElementById("document-types");

  try {
    const documentTypes = await getDocumentTypes();
    renderDocumentTypes(container, documentTypes);
  } catch (error) {
    showMessage(error.message, "danger");
  }
}

export async function handleDeleteDocumentType(documentTypeId) {
  try {
    const data = await deleteDocumentType(documentTypeId);

    showMessage(data.message, "success");

    await loadDocumentTypes();
  } catch (error) {
    showMessage(error.message, "danger");
  }
}
