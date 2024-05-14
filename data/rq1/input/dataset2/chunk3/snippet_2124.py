#Source: https://stackoverflow.com/questions/59220623/my-cached-function-throws-typeerror-decorated-with-lru-cache
@functools.lru_cache(maxsize=None)
def flat_map(map_: Dict[str, List[str]], start: str) -> Dict[str, List[str]]:
    if start not in map_:
        return []
    stars = map_[start] + [s for star in map_[start] for s in flat_map(star)]
    return {star: stars for star in starmap}