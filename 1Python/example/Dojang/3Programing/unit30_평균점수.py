def get_min_max_score(*args):
    min_score = min(tuple(args))
    max_score = max(tuple(args))
    return min_score, max_score

def get_average(*args):
    average_score = sum(tuple(args))/len(args)
    return average_score


if __name__ == '__main__':
    kor, eng, mat, sci = map(int, input().split())
    min_score, max_score = get_min_max_score(kor, eng, mat, sci)
    average_score = get_average(kor, eng, mat, sci)
    print(f'low score: {min_score:.2f}, high score: {max_score:.2f}, avg score: {average_score}')

    min_score, max_score = get_min_max_score(eng, sci)
    average_score = get_average(eng, sci)
    print(f'low score: {min_score:.2f}, high score: {max_score:.2f}, avg score: {average_score}')