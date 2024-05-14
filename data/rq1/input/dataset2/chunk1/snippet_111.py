#Source: https://stackoverflow.com/questions/72903946/attributeerror-forkawarelocal-object-has-no-attribute-connection-even-wit
if __name__ == "__main__":
    start = time.perf_counter()
    with Manager() as manager:
        genome_score_avgs = manager.list()
        processes = [Process(target=compareGenomes, args=(chunk, genome_score_avgs,)) for chunk in divideGenomes('TEST_DIR')]
        for p in processes:
            p.start()
        for p in processes:
            p.join()
    print(genome_score_avgs)
    print(*createTimeline(genome_score_avgs), sep='\n')
    print(f'Finished in {time.perf_counter() - start} seconds')