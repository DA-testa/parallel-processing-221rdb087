# python 3
import heapq

def parallel_processing(n, m, data):
    output = []
    threads = [(0, i) for i in range(n)]
    heapq.heapify(threads)
    for i in range(m):
        time, thread_id = heapq.heappop(threads)
        output.append((thread_id, time))
        heapq.heappush(threads, (time+data[i], thread_id))
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for pair in result:
        print(pair[0], pair[1])

if __name__ == "__main__":
    main()
