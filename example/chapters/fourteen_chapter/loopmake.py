dashes = "\n" + "-"*50
exec_dict = {
    "f":"""
for %s in %s:
    print %s
""",
    "s":"""
%s=0
%s = %s
while %s < len(%s):
    print %s[%s]
    %s = %s + 1
""",
    "n":"""
%s = %d
while %s < %d:
    print %s
    %s = %s + %d
"""
    }
def main():
    ltype = raw_input("loop type?(for/while)")
    dtype = raw_input("data type?(number/seq)")
    if dtype == "n":
        start = input("starting value?")
        stop = input("ending value(non-inclusive)?")
        step = input("stepping value?")
        seq = str(range(start, stop, step))
    else:
        seq = raw_input("enter sequence:")
    var = raw_input("iterative variable name?")
    if ltype == "f":
        exec_str = exec_dict["f"] % (var, seq, var)
    elif ltype == "w":
        if dtype == "s":
            svar = raw_input("enter sequence name?")
            exec_str = exec_dict["s"] %\
                       (var, svar, seq, var, svar, svar, var,var,var)
        elif dtype == "n":
            exec_str = exec_dict["n"] %\
                       (var, start, var, stop, var, var, var, step)
    print dashes
    print "your custom-generated code:" + dashes
    print exec_str + dashes
    print "test execution of the code:" + dashes
    exec exec_str
    print dashes

if __name__ == "__main__":
    main()