def test_app_is_creadted(app):
    assert app.name == 'atividade_KaBuM.app'

def test_should_return_sucesso_when_status_code_request_get_it_200(client):
    assert client.get("http://127.0.0.1:5000/v1/").status_code == 200

def test_should_return_sucesso_when_status_code_request_post_it_400(client):
    assert client.post("http://127.0.0.1:5000/v1/calculate-shipping").status_code == 400
