from loadDataset import load_dataset, print_dataset


def trainer(dataPath: str):
    dataset = load_dataset(dataPath)
    print_dataset(dataset)
    pass
