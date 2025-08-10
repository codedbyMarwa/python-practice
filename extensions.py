extension=input("Enter file's name with extension: ").strip().lower()
if extension.endswith("gip"):
    print("image/gip")
elif extension.endswith("jpg"):
    print("image/jpg")
elif extension.endswith("jpeg"):
    print("image/jpeg")
elif extension.endswith("png"):
    print("image/png")
elif extension.endswith("pdf"):
    print("document/pdf")
elif extension.endswith("txt"):
    print("textfile/txt")
elif extension.endswith("zip"):
    print("files/zip")
else:
    print("appliation/octet-stream")