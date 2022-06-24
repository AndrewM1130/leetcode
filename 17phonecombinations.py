from itertools import product

mapping = {
    '2': ["a","b","c"],
    '3': ["d","e","f"],
    '4': ["g","h","i"],
    '5': ["j","k","l"],
    '6': ["m","n","o"],
    '7': ["p","q","r","s"],
    '8': ["t","u","v"],
    '9': ["w","x","y","z"],
    '0': [" "]
    }

digits = "2"
total = [mapping[i]for i in digits]
combs = product(*total)
print(["".join(i) for i in combs])

def main():
    comb(args)

if __name__ == "__main__":
    main()
