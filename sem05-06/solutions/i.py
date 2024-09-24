def main():
	arr = [int(e) for e in input().split()]
	print(
    	"YES"
        if (
        	sum(arr) > 2
            or sum(arr) == 2
            and not any(arr[i] == arr[i + 1] == 1 for i in range(0, len(arr) - 1))
        )
        else "NO"
    )

if __name__ == "__main__":
    main()
