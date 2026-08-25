import { icons } from "../icons.js";
import { handleDeleteDocumentType } from "./controller.js";

export function renderDocumentTypes(container, documentTypes) {
  container.innerHTML = "";

  if (documentTypes.length === 0) {
    container.textContent = "No hay tipos de documento registrados.";
    return;
  }

  // dataset
  const updateUrl = container.dataset.updateUrl;

  documentTypes.forEach((docType) => {
    const element = document.createElement("div");
    element.textContent = docType.name;
    element.classList.add("element");

    const div = document.createElement("div");
    div.classList.add("actions");

    // edit
    const link = document.createElement("a");
    link.href = updateUrl.replace("0", docType.id);
    link.innerHTML = icons.pencil;
    link.classList.add("edit-btn");

    // delete
    const button = document.createElement("button");
    button.innerHTML = icons.trash;
    button.classList.add("delete-btn");

    button.addEventListener("click", () => {
      handleDeleteDocumentType(docType.id);
    });

    div.appendChild(link);
    div.appendChild(button);
    element.appendChild(div);
    container.appendChild(element);
  });
}
