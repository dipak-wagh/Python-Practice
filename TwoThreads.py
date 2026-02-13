import threading

def DisplayEven():
    print("First 10 even numbers: ")
    for i in range(2,20,2):
        print(i,end=" ")

def DisplayOdd():
    print("First 100 odd numbers: ")
    for i in range(1,200,3):
        print(i,end=" ")

def main():
    Even = threading.Thread(target=DisplayEven)
    Odd = threading.Thread(target=DisplayOdd)

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

    print("Both Threads Execution Complete.")
if __name__ == "__main__":
    main()