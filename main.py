# python3

def parallel_processing(n, m, data):
    # create a list of tuples to store the finishing time and thread index for each job
    finish_time = [(0, i) for i in range(n)]
    output = []

    for i in range(m):
        # find the thread with the earliest finishing time
        next_thread = min(finish_time)
        # update the finish time for the chosen thread
        finish_time[next_thread[1]] = (next_thread[0] + data[i], next_thread[1])
        # add the output pair to the list
        output.append((next_thread[1], next_thread[0]))

    return output


def main():
    # read input from keyboard
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # call the parallel_processing function
    result = parallel_processing(n, m, data)

    # print the output
    for i in range(m):
        print(result[i][0], result[i][1])


if __name__ == "__main__":
    main()

