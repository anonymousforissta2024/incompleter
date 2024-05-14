#Source: https://stackoverflow.com/questions/53095195/typeerror-unsupported-operand-types-for-builtin-function-or-method-and
fout = open(path + "/log.txt", "w")
while (True):
    mini_batch = train_graph_data.sample(config.batch_size)
    loss = model.fit(mini_batch)
    batch_n += 1
    if train_graph_data.is_epoch_end:
        epochs += 1
        batch_n = 0
        loss = 0
        if epochs % config.display == 0:
            embedding = None
            while (True):
                mini_batch = train_graph_data.sample(config.batch_size, do_shuffle=False)
                loss += model.get_loss(mini_batch)
                if embedding is None:
                    embedding = model.get_embedding(mini_batch)
                else:
                    embedding = np.vstack((embedding, model.get_embedding(mini_batch)))
                if train_graph_data.is_epoch_end:
                    break
            if config.check_reconstruction:
                print >> fout, epochs, "reconstruction:", check_reconstruction(embedding, train_graph_data,
                                                                               config.check_reconstruction)
            if config.check_link_prediction:
                print >> fout, epochs, "link_prediction:", check_link_prediction(embedding, train_graph_data,
                                                                                 origin_graph_data,
                                                                                 config.check_link_prediction)
            if config.check_classification:
                data = train_graph_data.sample(train_graph_data.N, do_shuffle=False, with_label=True)
                print >> fout, epochs, "classification", check_multi_label_classification(embedding, data.label)
            fout.flush()
            model.save_model(path + '/epoch' + str(epochs) + ".model")
        if epochs == config.epochs_limit:
            print("exceed epochs limit terminating")
            break