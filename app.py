from flask import Flask, request, jsonify
from rule_engine import create_rule, combine_rules, evaluate_rule

app = Flask(__name__)

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    rule_string = request.json.get('rule_string')
    rule_ast = create_rule(rule_string)
    return jsonify({"rule_ast": rule_ast})

@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    rules = request.json.get('rules')
    combined_ast = combine_rules(rules)
    return jsonify({"combined_ast": combined_ast})

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    data = request.json.get('data')
    ast = request.json.get('ast')
    result = evaluate_rule(ast, data)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
