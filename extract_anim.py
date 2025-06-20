import hou


def create_main_subnet(alembic_input):
    subnet_node = hou.node("/obj").createNode("subnet", "extract_animation")
    divide_geo_node = subnet_node.createNode("geo", "divide_into_parts")

    obj_merge = divide_geo_node.createNode("object_merge", "merge_alembic")
    obj_merge.parm('objpath1').set(alembic_input)
