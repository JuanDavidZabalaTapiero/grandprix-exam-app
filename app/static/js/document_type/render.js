import { icons } from "../icons.js";
import { handleDeleteDocumentType } from "./controller.js";

export function renderDocumentTypes(container, documentTypes) {
  container.innerHTML = "";

  if (documentTypes.length === 0) {
    container.textContent = "No hay tipos de documento registrados.";
    return;
  }

  // datasets
  const updateUrl = container.dataset.updateUrl;

  documentTypes.forEach((docType) => {
    const element = document.createElement("div");
    element.textContent = docType.name;

    // edit
    const link = document.createElement("a");
    link.href = updateUrl.replace("0", docType.id);
    link.innerHTML = icons.pencil;

    // delete
    const button = document.createElement("button");
    button.innerHTML = icons.trash;

    button.addEventListener("click", () => {
      handleDeleteDocumentType(docType.id);
    });

    element.appendChild(link);
    element.appendChild(button);
    container.appendChild(element);
  });
}
