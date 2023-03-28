# python3

def parallel_processing(n, m):
    assigned_jobs = [[] for _ in range(n)]
    threads = [(i, 0) for i in range(n)]
    for job in m:
        thread_id, completion_time = min(threads, key=lambda x: (x[1], x[0]))
        assigned_jobs[thread_id].append(completion_time)
        threads[thread_id] = (thread_id, completion_time + job)
    return assigned_jobs

def main():
    n, m = map(int, input().split())
    m = list(map(int, input().split()))
    result = parallel_processing(n, m)
    for times in result:
        for time in times:
            print(time, end=' ')
        print()


if __name__ == "__main__":
    main()
