# def main():
#     No1 = int(input())
#     No2 =int(input())

#     print(No1 + No2)

# if __name__ == "__main__":
#     main()

import sys

def main():
    print(sys.argv[0])
    print(sys.argv[1])
    print(len(sys.argv))

if __name__ == "__main__":
    main()