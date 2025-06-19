import sys

def main():
    if len(sys.argv) <= 1:
        print("none")
        return

    for arg in sys.argv[1:]:
        print(f"{arg}ZZZZZ$")

if __name__ == "__main__":
    main()