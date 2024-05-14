#Source: https://stackoverflow.com/questions/74975478/ai-text-generator-returning-attributeerror-cant-set-attribute
ai.train(file_name,
     line_by_line = False,
     from_cache = False,
     num_steps = 3000,
     generate_every = 1000,
     save_every = 1000,
     save_gdrive = False,
     learning_rate = 1e-3,
     fp16 = True, 
     batch_size = 1,
     )