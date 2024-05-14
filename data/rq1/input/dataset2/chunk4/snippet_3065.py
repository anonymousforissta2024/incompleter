#Source: https://stackoverflow.com/questions/76268924/timm-attributeerror-dataparallel-object-has-no-attribute-items
ptcfg = timm.models.registry.get_pretrained_cfg('swin_base_patch4_window7_224')
ptcfg['file'] = 'model_swin.pth'
model = torch.nn.DataParallel(timm.models.swin_base_patch4_window7_224(pretrained=True, pretrained_cfg=ptcfg, drop_path_rate=0.2), device_ids=[0,1])
model.eval()