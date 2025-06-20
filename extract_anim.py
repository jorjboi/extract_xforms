import hou


def create_main_subnet():
    subnet_node = hou.node("/obj").createNode("subnet", "extract_animation")
    subnet_node.moveToGoodPosition()
    return subnet_node


def create_divide_into_parts_geo_node(parent_node):
    divide_geo_node = parent_node.createNode("geo", "divide_into_parts")
    divide_geo_node.moveToGoodPosition()
    return divide_geo_node


def divide_into_parts(parent_node, alembic_path):
    obj_merge = parent_node.createNode("object_merge", "merge_alembic")
    obj_merge.moveToGoodPosition()
    obj_merge.parm('objpath1').set(alembic_path)
    return obj_merge


def main(alembic_path):
    subnet_node = create_main_subnet()
    divide_node = create_divide_into_parts_geo_node(subnet_node)
    divide_into_parts(divide_node, alembic_path)
