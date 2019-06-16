def get_steps(code):
    code = str.upper(code)
    steps = []
    for i in range(code.count("X")):
        steps.append(code[:code.find("X")])
        code = code[code.find("X")+1:]
    steps.append(code)
    inst = []
    for step in steps:
        drinks = []
        for i in range(step.count("N")):
            drinks.append(step[:step.find("N")])
            step = step[step.find("N")+1:]
        drinks.append(step)
        inst.append(drinks)
    out = []
    for i in inst:
        y = []
        for q in i:
            x = []
            x.append(q[:q.find("Q")])
            q = q[q.find("Q")+1:]
            x.append(q)
            y.append(x)
        out.append(y)
    return out

try:
    while True:
        code = input("geef de code aub")
        instr = get_steps(code)
        print(instr)
except Exception as e:
    print(e)
finally:
    print("gestopt")