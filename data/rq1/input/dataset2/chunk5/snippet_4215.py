#Source: https://stackoverflow.com/questions/59260545/attributeerror-module-object-has-no-attribute-signature-tensorflow1-15-an
model = load_model(
    "../../deepposekit-data/datasets/fly/best_model_densenet.h5",
    augmenter=augmenter,
    generator=data_generator,
)