from ast import Node

def create_rule(rule_string):
    
    return Node("operator", left=Node("operand", value="age"), right=Node("operand", value=30))

def combine_rules(rules):
    combined_node = Node("operator", left=create_rule(rules[0]), right=create_rule(rules[1]))
    return combined_node

def evaluate_rule(ast, data):
    if ast.node_type == "operand":
        return data[ast.value] > 30  
    
    return False
