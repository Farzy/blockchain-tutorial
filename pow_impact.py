from hashlib import sha256
import timeit


# Exemple showing that looking for a hash that starts with 8 or more zeros takes a very
# long time.
# $ python pow_impact.py
# (21, '0512850a5bd546154cd383bfb712b7b18b97593dffc04e5ab0eeb9568838c9f7')
# Execution time: 0.00018929402s
# (100, '00c337b1d003baeb8068c63e3324d943a018ccdd0c36850897833fb89c0a191b')
# Execution time: 0.00032319099s
# (2241, '000032a855911b16ac15945655eb6e3ab205de6eeb5fd1f2221fe456a7ce4cf5')
# Execution time: 0.007204791s
# (2241, '000032a855911b16ac15945655eb6e3ab205de6eeb5fd1f2221fe456a7ce4cf5')
# Execution time: 0.007332598s
# (2588371, '00000a14170906d8ada9acaa48e05d1f47888dda59c68a0d3b9672a11941b4c0')
# Execution time: 5.9141482s
# (17985707, '000000fea0ea59b5f3f7d595f9defcb848946b843c40c9e53071ae06faf92b8b')
# Execution time: 40.315048s
# (369706652, '00000000ec6b2cc307a60742b33e5b59045ce1dd65b732209ba6404bca686df3')
# Execution time: 834.4031s
# (369706652, '00000000ec6b2cc307a60742b33e5b59045ce1dd65b732209ba6404bca686df3')
# Execution time: 812.54892s


def compute(zeros: int):
    nonce = 0
    msg = "GNU/Linux Magazine"
    my_hash = ''
    while not my_hash.startswith('0' * zeros):
        nonce += 1
        my_hash = sha256(bytes(sha256(bytes((str(nonce) + msg).encode())).hexdigest().encode())).hexdigest()
    return nonce, my_hash


if __name__ == '__main__':
    for i in range(1, 4):
        print("Execution time: {:.8G}s".format(timeit.timeit(lambda n=i: print(compute(i)), number=1)))
