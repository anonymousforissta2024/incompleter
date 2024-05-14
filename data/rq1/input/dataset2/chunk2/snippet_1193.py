#Source: https://stackoverflow.com/questions/67606204/pytorch-training-an-lstm-attributeerror-nonetype-object-has-no-attribute-c
checkpoint_dir = '/content/gdrive/MyDrive/Checkpoint_dir'
data_dir = './data'

epochs=5

def custom_train_part(config, checkpoint_dir=None, data_dir=None):
    model = LSTM(len(True_IMF_df.T), config["Hidden"], config["Layers"], 1)
    

    device = "cpu"
    if torch.cuda.is_available():
        device = "cuda:0"
        if torch.cuda.device_count() > 1:
            model = nn.DataParallel(model)
    model.to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=config["lr"])
    criterion = nn.MSELoss()

    if checkpoint_dir:
        model_state, optimizer_state = torch.load(
            os.path.join(checkpoint_dir, "checkpoint"))
        model.load_state_dict(model_state)
        optimizer.load_state_dict(optimizer_state)
    
    for e in range(epochs):

        running_loss = 0.0
        epoch_steps = 0
        
        model.train()  # put model to training mode
        x = x_hht_train.to(device)
        y = y_hht_train.to(device)

        scores = model(x)
        loss = criterion(scores, y_hht_train)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        print(f"Running loss: {running_loss}")
        epoch_steps += 1

        if e % 5 == 0:
            print(f'Epoch: {e}, loss = {loss.cpu().item()}')
            # check_accuracy(loader_val, model)
            print()
    
        # Validation loss
        val_loss = 0.0
        val_steps = 0
        total = 0
        correct = 0
        
        with torch.no_grad():
            x = x_hht_val.to(device)  # move to device, e.g. GPU
            y = y_hht_val.to(device)

            scores = model(x)
            scores = scores.cpu()
            y = y.cpu()
            correct += (np.sign(scores) == np.sign(y)).sum().item()
            print(f"Correct: {correct}")

            loss = criterion(scores, y)
            print(f"Val Loss: {loss.item()}")
            val_loss += loss.cpu()
            val_steps += 1

        with tune.checkpoint_dir(e) as checkpoint_dir:
            path = os.path.join(checkpoint_dir, "checkpoint")
            torch.save((model.state_dict(), optimizer.state_dict()), path)

        tune.report(loss=(val_loss / val_steps), accuracy = correct / len(y_hht_val))
    print("Finished Training")



config = {
    "lr": tune.loguniform(1e-6, 1e-1),
    "Layers": tune.sample_from(lambda _: np.random.randint(1, 10)),
    "Hidden" : tune.sample_from(lambda _: np.random.randint(2, 100))
}

scheduler = ASHAScheduler(
        metric="loss",
        mode="min",
        max_t=10,
        grace_period=1,
        reduction_factor=2)

reporter = CLIReporter(
    #parameter_columns=["lr", "Layers", "Hidden"],
    metric_columns=["loss", "accuracy", "training_iteration"]
)

result = tune.run(
    custom_train_part,
    resources_per_trial={"cpu": 4, "gpu": 1},
    config=config,
    num_samples=1,
    scheduler = scheduler,
    progress_reporter=reporter
)

print(f"Results: {result.get_best_config(metric = 'loss', mode = 'min')}")

best_trial = result.get_best_trial(metric = "loss", mode = "min")

print("Best trial config: {}".format(best_trial.config))
print("Best trial final validation loss: {}".format(
    best_trial.last_result["loss"]))
print("Best trial final validation accuracy: {}".format(
    best_trial.last_result["accuracy"]))

##############################################################
#                       AFTER TUNNING                       #
##############################################################

best_trained_model = LSTM(len(True_IMF_df.T), best_trial.config["Hidden"], best_trial.config["Layers"], 1)
best_checkpoint_dir = best_trial.checkpoint.value
model_state, optimizer_state = torch.load(os.path.join(
    best_checkpoint_dir, "checkpoint"))
best_trained_model.load_state_dict(model_state)