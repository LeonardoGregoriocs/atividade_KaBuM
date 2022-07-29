import json

from flask import Blueprint, request, Response

from atividade_KaBuM.application.service.service_shipping import ServiceShipping


blueprint = Blueprint('api', __name__, url_prefix='/v1')


@blueprint.route("/", methods=['GET'])
def index():
    return 'Sistema utilizado para consultar opções de transportes dos produtos.'

@blueprint.route("/calculate-shipping", methods=['POST'])
def get_info():
    try:
        request_json = request.get_json()

        dimension = request_json['dimensao']
        weight = request_json['peso']

        width = dimension['largura']
        height = dimension['altura']

        service_shipping = ServiceShipping()
        service_obj = service_shipping.calculate_shipping(weight, width, height)

        if service_obj:
            return json.dumps(service_obj)
        return "[]"

    except Exception as e:
        msg = 'Solicitação inválida, falta informações.'
        return return_error(msg, 400)

def return_error(message, status):
    response_json = json.dumps({'error-message': message})
    return Response(response_json, status, mimetype='application/json')