# python3

def parallel_processing(n, m, data):
    time = [(0, i) for i in range(n)]
    output = []

    for i in range(m):
        thread = min(time)
        time[thread[1]] = (thread[0] + data[i], thread[1])
        output.append((thread[1], thread[0]))

    return output


def main():

    n, m = map(int, input().split())
    data = list(map(int, input().split()))

  
    result = parallel_processing(n, m, data)


    for i in range(m):
        print(result[i][0], result[i][1])


if __name__ == "__main__":
    main()

