def log_result(result):
    with open('result.txt', 'a', encoding='utf-8') as data:
        data.write(f'{str(result)}\n')

