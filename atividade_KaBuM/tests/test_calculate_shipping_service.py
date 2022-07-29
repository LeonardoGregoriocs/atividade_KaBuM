from ..application.service.service_shipping import calculate_shipping_value, to_json, validate_shipping, ServiceShipping


def test_should_return_empty_if_not_have_shipping():
    service_shipping = ServiceShipping()

    result = service_shipping.calculate_shipping(5600, 162, 230)

    expected_result = []

    assert result == expected_result

def test_should_return_shipping_kabum():
    service_shipping = ServiceShipping()

    result = service_shipping.calculate_shipping(400, 40, 6)

    expected_result = {
        "Nome":"Entrega Kabum",
        "Valor_frete": 8.0,
        "Prazo_dias": 4
	}

    assert result == expected_result

def test_should_return_shipping_ninja():
    service_shipping = ServiceShipping()

    result = service_shipping.calculate_shipping(850, 50, 152)

    expected_result = {
        "Nome": "Entrega Ninja",
        "Valor_frete": 25.50,
        "Prazo_dias": 6
    }

    assert result == expected_result

def test_should_return_shipping_ninja_and_kabum():
    service_shipping = ServiceShipping()

    result = service_shipping.calculate_shipping(400, 40, 102)

    expected_result = {
        "Nome": "Entrega Ninja",
        "Valor_frete": 12.0,
        "Prazo_dias": 6
    },{
        "Nome": "Entrega Kabum",
        "Valor_frete": 8.0,
        "Prazo_dias": 4
    }

    assert result == expected_result

def test_should_calculate_shipping_value_kabum():

    assert 8.0 == calculate_shipping_value(400, 0.2)

def test_should_calculate_shipping_value_ninja():

    assert 12.0 == calculate_shipping_value(400, 0.3)

def test_should_return_a_json_shipping_kabum():

    json_obj = {
        "Nome" : "Entrega KaBuM",
        "Valor_frete" : 12.0,
        "Prazo_dias" : 4
    }

    shipping_json_kabum = to_json(12.0, "Entrega KaBuM", 4)

    assert json_obj == shipping_json_kabum

def test_should_return_a_json_shipping_ninja():

    json_obj = {
        "Nome" : "Entrega Ninja",
        "Valor_frete" : 8.0,
        "Prazo_dias" : 6
    }

    shipping_json_ninja = to_json(8.0, "Entrega Ninja", 6)

    assert json_obj == shipping_json_ninja

def test_should_return_if_ninja_shipping_is_valid():

    result = validate_shipping(40, 102, 400, 140, 6, 200, 6, 0.3, "Entrega Ninja", 6)

    expected_result = {
        "Nome": "Entrega Ninja",
        "Valor_frete": 12.0,
        "Prazo_dias": 6
    }

    assert result == expected_result

def test_should_return_if_ninja_shipping_is_not_valid_due_width():

    result = validate_shipping(160, 40, 400, 140, 6, 200, 6, 0.3, "Entrega Ninga", 6)

    expected_result = []

    assert result == expected_result

def test_should_return_if_ninja_shipping_is_not_valid_due_height():

    result = validate_shipping(100, 210, 400, 140, 6, 200, 6, 0.3, "Entrega Ninga", 6)

    expected_result = []

    assert result == expected_result

def test_should_return_if_kabum_shipping_is_valid():

    result = validate_shipping(40, 102, 400, 125, 13, 140, 5, 0.2, "Entrega Kabum", 4)

    expected_result = {
        "Nome": "Entrega Kabum",
        "Valor_frete": 8.0,
        "Prazo_dias": 4
    }

    assert result == expected_result

def test_should_return_if_kabum_shipping_is_not_valid_due_width():

    result = validate_shipping(160, 40, 400, 125, 13, 140, 5, 0.2, "Entrega Kabum", 4)

    expected_result = []

    assert result == expected_result

def test_should_return_if_kabum_shipping_is_not_valid_due_height():

    result = validate_shipping(40, 150, 400, 125, 13, 140, 5, 0.2, "Entrega Kabum", 4)

    expected_result = []

    assert result == expected_result
