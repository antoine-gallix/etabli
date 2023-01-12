def vars():
    for v in list(filter(lambda name: not (name[:2] == "__"), locals().keys())):
        print(v)
