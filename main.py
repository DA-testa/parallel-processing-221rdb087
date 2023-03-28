# python3

def parallel_processing(n, m, data):
    output = []
    jobs = list(enumerate(data))
    finish_times = [0] * n
    for job in jobs:
        earliest_finish_time = min(finish_times)
        earliest_finish_thread = finish_times.index(earliest_finish_time)
        finish_times[earliest_finish_thread] += job[1]
        output.append((job[0], earliest_finish_thread))
        
    return output

def main():
   
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for pair in result:
        print(pair[0], pair[1])

if __name__ == "__main__":
    main()
