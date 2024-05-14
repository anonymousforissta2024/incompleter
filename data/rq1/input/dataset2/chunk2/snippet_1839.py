#Source: https://stackoverflow.com/questions/55794829/how-to-solve-the-error-attributeerror-type-object-image-has-no-attribute-op
b1 = Button(root, text="Elbow Method", command=plot_elbow, bg="green", fg="white").pack(side = LEFT)
b2 = Button(root, text="K-Means Clustering", command=plot_kmeans, bg="blue", fg="white").pack(side = LEFT)
b3 = Button(root, text="Batsmen who scored 4 or more Hundreds", command=plot_hundreds, bg="#D35400", fg="white").pack(side = LEFT)
b4 = Button(root, text="Runs Scored by Various Players", command=plot_runs, bg="#117A65", fg="white").pack(side = LEFT)
b5 = Button(root, text="Best Batsmen", command=plot_best_batsmen, bg="#34495E", fg="white").pack(side = LEFT)
b6 = Button(root, text="Stop", command=root.destroy, bg="red", fg="white").pack(side = BOTTOM)