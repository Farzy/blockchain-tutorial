from hashlib import sha256
import timeit


def compute(zeros: int):
    nonce = 0
    msg = "GNU/Linux Magazine"
    my_hash = ''
    while not my_hash.startswith('0' * zeros):
        nonce += 1
        my_hash = sha256(bytes(sha256(bytes((str(nonce) + msg).encode())).hexdigest().encode())).hexdigest()
    return nonce, my_hash


if __name__ == '__main__':
    for i in range(1, 6):
        print(timeit.timeit(lambda n=i: print(compute(i)), number=1))
