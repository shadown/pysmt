from pysmt.shortcuts import And, Symbol, LE, GE, Int, Equals, Plus, Times, is_sat
from pysmt.typing import INT


hello = [Symbol(s, INT) for s in "hello"]
world = [Symbol(s, INT) for s in "world"]

letters = set(hello+world)

domains = And([And( LE(Int(1), l),
                    GE(Int(10), l) ) for l in letters])


sum_hello = Plus(hello)
sum_world = Plus(world)


problem = And(Equals(sum_hello, sum_world),
              Equals(sum_hello, Int(25)))

formula = And(domains, problem)

print "Serialization of the formula:"
print formula

print "Checking Satisfiability:"
print is_sat(formula)
