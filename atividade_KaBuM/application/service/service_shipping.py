from atividade_KaBuM.utils.constants import *


class ServiceShipping():

    def calculate_shipping(self, weight, width, height):

        shipping_kabum = validate_shipping(
            width,
            height,
            weight,
            width_max_kabum,
            width_min_kabum,
            height_max_kabum,
            height_min_kabum,
            value_const_kabum,
            name_kabum,
            delivery_deadline_kabum
        )

        shipping_ninja = validate_shipping(
            width,
            height,
            weight,
            width_max_ninja,
            width_min_ninja,
            height_max_ninja,
            height_min_ninja,
            value_const_ninja,
            name_ninja,
            delivery_deadline_ninja
        )

        if shipping_ninja == [] and shipping_kabum != []:
            return shipping_kabum

        elif shipping_ninja != [] and shipping_kabum == []:
            return shipping_ninja

        elif shipping_ninja == [] and shipping_kabum == []:
            return []

        else:
            return shipping_ninja, shipping_kabum

def validate_shipping(width, height, weight, width_max, width_min, height_max,  height_min, value_const, name, delivery_deadline):

    if width > width_max or width < width_min:
        return []

    if height > height_max or height < height_min:
        return []

    shipping_value = calculate_shipping_value(weight, value_const)

    shipping_obj_json = to_json(shipping_value, name, delivery_deadline)

    if shipping_obj_json:
        return shipping_obj_json

def calculate_shipping_value(weight: int, value_const) -> float:
    shipping_value = (weight * value_const) / 10

    return shipping_value

def to_json(shipping_value, option_shipping, delivery_deadline):
    shipping_json = {
        "Nome" : option_shipping,
        "Valor_frete" : shipping_value,
        "Prazo_dias" : delivery_deadline
    }

    return shipping_json