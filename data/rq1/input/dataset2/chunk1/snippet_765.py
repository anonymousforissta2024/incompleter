#Source: https://stackoverflow.com/questions/75939176/default-collate-typeerror-batch-must-contain-tensors-numbers-dicts-or-lists
def get_dataloader(slide_ids: List[str], tile_filenames: List[Path]) -> DataLoader:
    dataset = ApplicationDataset(slide_ids, tile_filenames)

    return DataLoader(dataset, batch_size=1, shuffle=False, num_workers=1, collate_fn=ApplicationDataset.collate)