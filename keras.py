class FeaturesExtractor:
    '''Runs pretrained model without top layers on dataset and saves generated
    bottleneck features onto disk
    '''

    def __init__(self, build_fn, preprocess_fn, source,
                 target_size=(299, 299, 3), batch_size=128):
        self.build_fn = build_fn
        self.preprocess_fn = preprocess_fn
        self.source = source
        self.target_size = target_size
        self.batch_size = batch_size

    def __call__(self, folder, filename, pool='avg'):
        model = self.build_fn(weights='imagenet', include_top=False, pooling=pool)
        stream = self.source(
            folder=folder, target_size=self.target_size,
            batch_size = self.batch_size, infinite=False)

        batches = []
        with tqdm.tqdm