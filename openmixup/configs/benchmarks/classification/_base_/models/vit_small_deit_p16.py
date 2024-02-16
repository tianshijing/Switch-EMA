# model settings
model = dict(
    type='MixUpClassification',
    pretrained=None,
    alpha=[0.8, 1.0,],  # deit setting
    mix_mode=["mixup", "cutmix",],
    mix_args=dict(),
    backbone=dict(
        type='MIMVisionTransformer',
        arch='deit-small',  # 12 layers DeiT-S with finetune
        img_size=224,
        patch_size=16,
        drop_path_rate=0.1,
        final_norm=False,
        finetune=True),
    head=dict(
        type='ClsMixupHead',  # mixup CE + label smooth
        loss=dict(type='LabelSmoothLoss',
            label_smooth_val=0.1, num_classes=1000, mode='original', loss_weight=1.0),
        with_avg_pool=False,  # no gap in ViT
        in_channels=384, num_classes=1000),
)