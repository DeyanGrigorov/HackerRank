def minTime(files, numCores, limit):
    if numCores == 1:
        result = 0
        for file in files:
            result += file
        return print(result)
    elif numCores > 1:
        if limit == 1:
            max_file = max(files)
            parallel = int(max_file / numCores)
            result_files = 0
            files.remove(max_file)
            for file in files:
                result_files += file
            result = result_files + parallel
            return print(result)
        elif limit > 1:
            new_list = []
            parallel_res = 0
            for file in files:
                if file % numCores == 0:
                    new_list.append(file)
            if limit != len(new_list):
                results = []
                for file in new_list:
                    results.append(file / numCores)
                for file in new_list:
                    files.remove(file)
                result = int(sum(files)) + int(sum(results))
                return result


if __name__ == '__main__':

    files_count = int(input().strip())

    files = []

    for _ in range(files_count):
        files_item = int(input().strip())
        files.append(files_item)

    numCores = int(input().strip())

    limit = int(input().strip())

    result = minTime(files, numCores, limit)
