from app.services.license_category import LicenseCategoryService


def test_get_all_categories_api_empty(client):
    response = client.get("/api/license-categories/")

    assert response.status_code == 200
    assert response.get_json() == {"categories": []}


def test_get_all_categories_api_success(client):
    LicenseCategoryService.create("A2")
    LicenseCategoryService.create("B1")

    response = client.get("/api/license-categories/")

    assert response.status_code == 200

    data = response.get_json()
    assert len(data["categories"]) == 2
    assert data["categories"][0]["name"] == "A2"
    assert data["categories"][1]["name"] == "B1"


def test_delete_category_api_success(client):
    category = LicenseCategoryService.create("A2")

    response = client.delete(f"/api/license-categories/{category.id}")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Categoría eliminada correctamente."}


def test_delete_category_api_not_found(client):
    response = client.delete("/api/license-categories/999")

    assert response.status_code == 404
    assert response.get_json() == {"message": "La categoría con id 999 no existe."}
