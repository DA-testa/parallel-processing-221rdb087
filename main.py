# python 3
import heapq
def parallel_processing(n, m, data):
    output = []
    threads = [(i, 0) for i in range(n)]
    heapq.heapify(threads)
    for i in range(m):
        thread = heapq.heappop(threads)
        output.append((thread[0], thread[1]))
        heapq.heappush(threads, (thread[0], thread[1] + data[i]))
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for pair in result:
        print(pair[0], pair[1])

if __name__ == "__main__":
    main()
