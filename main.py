# python3

def parallel_processing(n, m, data):
    output = []
    threads = [(i, 0) for i in range(n)] 
    for i in range(m):
        thread = min(threads, key=lambda x: x[1]) 
        output.append((i, thread[0])) 
        threads[thread[0]] = (thread[0], thread[1] + data[i]) 
    return output


def main():
   
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for pair in result:
        print(pair[0], pair[1])

if __name__ == "__main__":
    main()
