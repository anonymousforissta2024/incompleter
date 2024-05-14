#Source: https://stackoverflow.com/questions/72064119/typeerror-after-vectorizing-a-function
df_test['in_range']=np.vectorize(within_range)(df=df_3,
                                   CoCode=df_test['BKPF-BUKRS'],
                                   Lease_type=df_test['COBL-AUFNR'].str[5:6],
                                   Position=df_test['BSEG-HKONT'].str[0:6],
                                   Mvt_Type=df_test['BSEG-HKONT'].str[6:],
                                   BKPF_WAERS=df_test['BKPF-WAERS'],
                                   BSEG_BSCHL=df_test['BSEG-BSCHL'],
                                   COBL_KOSTL=df_test['COBL-KOSTL'],
                                   Amount=df_test['BSEG-WRBTR'],
                                  )