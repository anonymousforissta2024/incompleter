#Source: https://stackoverflow.com/questions/45853644/migrate-from-python2-to-python-3-6-2-with-typeerror
f.writelines("%20s,%04d\n" % (varStr, varInt))
f.writelines('{0:>20s},{1:04d}\n'.format(varStr, varInt))