#Source: https://stackoverflow.com/questions/75704300/attributeerror-stablediffusionkdiffusionpipeline-object-has-no-attribute-sam
if not os.path.exists(IMAGE_SAVE_PATH):
    os.mkdir(IMAGE_SAVE_PATH)

def generate_image_name(prompt, ext='.png'):
    from uuid import uuid4
    return f"{IMAGE_SAVE_PATH}/{str(uuid4())}{prompt[:25].replace(' ', '-')}.{ext}"

pipe = StableDiffusionKDiffusionPipeline.from_pretrained(V5_MODEL_PATH, torch_dtype=torch.float16, revision='fp16')
pipe.to("cuda")
with autocast('cuda'):
    image = pipe(prompt).images[0]
image.save(generate_image_name(prompt))