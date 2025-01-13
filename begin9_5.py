try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")
#To indicate that an exception is a direct consequence of another, the raise statement allows an optional from clause

raise RuntimeError from exc
