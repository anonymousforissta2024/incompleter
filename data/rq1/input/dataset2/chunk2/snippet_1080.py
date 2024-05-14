#Source: https://stackoverflow.com/questions/70609503/how-to-fix-typeerror-caught-typeerror-in-dataloader-worker-process-1-in-detectr
from detectron2.engine import DefaultTrainer

# TOTAL_NUM_IMAGES = 10531

cfg = get_cfg()
cfg.OUTPUT_DIR = os.path.join('./output')
cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
cfg.DATASETS.TRAIN = ("my_dataset_train",)
cfg.DATASETS.TEST = ()
cfg.DATALOADER.NUM_WORKERS = 2
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")  # Let training initialize from model zoo
cfg.SOLVER.IMS_PER_BATCH = 2
cfg.SOLVER.BASE_LR = 0.00025  # pick a good LR

# single_iteration = cfg.SOLVER.IMS_PER_BATCH
# iterations_for_one_epoch = TOTAL_NUM_IMAGES / single_iteration
# cfg.SOLVER.MAX_ITER = int(iterations_for_one_epoch) * 20

cfg.SOLVER.STEPS = []        # do not decay learning rate
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1  # only has one class (person). (see https://detectron2.readthedocs.io/tutorials/datasets.html#update-the-config-for-new-datasets)
# NOTE: this config means the number of classes, but a few popular unofficial tutorials incorrect uses num_classes+1 here.

os.makedirs(cfg.OUTPUT_DIR, exist_ok=True)
trainer = DefaultTrainer(cfg) 
trainer.resume_or_load(resume=False)
trainer.train()