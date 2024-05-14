#Source: https://stackoverflow.com/questions/68922318/gwpy-package-gives-error-attributeerror-module-matplotlib-pyplot-has-no-att
print(matplotlib.get_backend()) # module://ipykernel.pylab.backend_inline
print(matplotlib.__version__) # 3.4.3
print(gwpy.__version__) # 2.0.4