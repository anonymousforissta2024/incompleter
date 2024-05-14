#Source: https://stackoverflow.com/questions/69750297/how-do-i-fix-a-typeerror-object-of-type-bytes-is-not-json-serializable-that-is
cutout_b64 = base64.b64encode(sbuffer.getvalue()).decode("ascii")