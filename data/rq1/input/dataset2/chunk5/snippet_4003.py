#Source: https://stackoverflow.com/questions/49265274/typeerror-a-bytes-like-object-is-required-not-row-spark-rdd-map
testing = t.select('XML_Data').rdd.map(xmlparse)