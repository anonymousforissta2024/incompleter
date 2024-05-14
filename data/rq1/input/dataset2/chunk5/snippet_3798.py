#Source: https://stackoverflow.com/questions/58824935/getting-typeerror-when-running-script-with-os-path-join
api_xml = os.path.join(opts.out, os.path.basename(
    opts.api_raw).replace('.raw', '.xml'))