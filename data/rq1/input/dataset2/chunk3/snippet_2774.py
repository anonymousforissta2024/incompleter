#Source: https://stackoverflow.com/questions/72380052/how-solved-python-text-processing-attributeerror-list-object-has-no-attribut
selct = StringVar()
categorychoosen = ttk.Combobox(top, width = 27, textvariable = selct)
categorychoosen['values'] = (' Computer Science', 
                          ' computer engineering',
                          ' Information Technology',
                          ' artificial intelligence',
                          ' cyber security',
                          ' computer networks',
                          ' Information Security',
                          ' Management Information Systems',
                          ' Software engineering',
                          ' data analysis',
                          ' Data Science')
  
categorychoosen.grid(row=1, column=2)
categorychoosen.current()

s = StringVar()
choosen = ttk.Combobox(top, width = 27, textvariable = s)
choosen['values'] = (' Computer Science', 
                          ' computer engineering',
                          ' Information Technology',
                          ' artificial intelligence',
                          ' cyber security',
                          ' computer networks',
                          ' Information Security',
                          ' Management Information Systems',
                          ' Software engineering',
                          ' data analysis',
                          ' Data Science')
  
choosen.grid(row=1, column=3)
choosen.current()

def model():
    
    from sklearn.model_selection import train_test_split
    from sklearn.feature_extraction.text import TfidfVectorizer
    from scipy.sparse import hstack
    from sklearn.multiclass import OneVsRestClassifier
    from sklearn.neighbors import KNeighborsClassifier

    resume = pd.read_csv(r'/Users/asma/Desktop/UpdatedResumeDataSet.csv')

    #DATA
    x = resume['Resume'].values
    y = resume['Category'].values
    v = [[selct.get(),s.get()]]

    #transform
    word = TfidfVectorizer(sublinear_tf=True, stop_words='english')
    word.fit(x)
    wordFeatures = word.transform(x)
    
    w = TfidfVectorizer(sublinear_tf=True, stop_words='english')
    w.fit(v)
    wx = word.transform(v)

    # to 2D Array
    wx.reshape(-1, 1)
    wordFeatures.reshape(-1, 1)
    x.reshape(-1, 1)

    #KNN 
    model = KNeighborsClassifier(n_neighbors=5, metric= 'euclidean')
    model.fit(wordFeatures,y)
    x_test = wx
    y_pred = model.predict([x_test])
    jobR = Label(top,text=str([y_pred]) ,bg='light gray').grid(row=4,column=2)

but= Button(top,text="Start",bg='gray', command=model).grid(row=3,column=0)