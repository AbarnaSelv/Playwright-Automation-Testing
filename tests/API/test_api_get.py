from playwright.sync_api import sync_playwright

def test_api_get():
    with sync_playwright() as p:
        request = p.request.new_context(
            extra_http_headers={
                "Accept": "application/json"
            }
        )

        response = request.get("https://reqres.in/api/users?page=2")

        assert response.status == 200

        json_data = response.json()
        print(json_data)

        assert json_data["data"][0]["id"] == 7

        request.dispose()