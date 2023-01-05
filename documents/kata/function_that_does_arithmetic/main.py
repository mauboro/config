def arithmetic(a, b, op):
    return a + b if op == "add" else a - b if op == "subtract" else a * b if op == "multiply" else a / b if op == "divide" else None


def arithmetic_refactored(a, b, op):
    return {
            "add": a + b,
            "subtract": a - b,
            "multiply": a * b,
            "divide": a / b
    }[op]
