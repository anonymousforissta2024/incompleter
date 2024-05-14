#Source: https://stackoverflow.com/questions/33987368/custom-float-entry-for-tkinter-throwing-attribute-error-upon-deleting-contents
self.depth_label = tk.Label(self, text="Maximum Depth")
self.depth_label.grid(row=1, column = 1)
self.depth_entry = FloatEntry(self, default=255.0)
self.depth_entry.grid(row=1, column = 2)