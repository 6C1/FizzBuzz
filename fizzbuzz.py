print "\n".join(["{}".format("FizzBuzz"[bool(i % 3) * 4:8 - 4 * bool(i % 5)] or i) for i in xrange(1, 101)])
