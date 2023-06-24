with open("input.json", "r") as rf:
    with open("formated.json", "w") as wf:
        wf.write('{"Jobs":')
        for line in rf:
            wf.write(line)
        wf.write("}")
