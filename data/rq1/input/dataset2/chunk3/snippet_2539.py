#Source: https://stackoverflow.com/questions/61109095/typeerror-nonetype-object-is-not-subscriptable-when-i-train-a-cnn-model
class Metrics(Callback):
    def on_train_begin(self, logs = {}):
        self.val_kappas = []

    def on_epoch_end(self, epoch, logs = {}):
        X_val, y_val = self.validation_data[:2]
        y_val = y_val.sum(axis = 1) - 1

        y_pred = self.model.predict(X_val) > 0.5
        y_pred = y_pred.astype(int).sum(axis = 1) - 1

        _val_kappa = cohen_kappa_score(
            y_val,
            y_pred, 
            weights = 'quadratic'
        )

        self.val_kappas.append(_val_kappa)

        print(f"val_kappa: {_val_kappa:.4f}")

        if _val_kappa == max(self.val_kappas):
            print("Validation Kappa has improved. Saving model.")
            self.model.save('/path_to/model.h5')

        return