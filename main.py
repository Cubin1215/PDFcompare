import hashlib


def hash_file(file1, file2):

    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

    with open(file1, "rb") as f1:
        a = f1.read()
        h1.update(a)
    with open(file2, "rb") as f2:
        b = f2.read()
        h2.update(b)

    return h1.hexdigest(), h2.hexdigest()


m1, m2 = hash_file("pd1.pdf", "pd2.pdf")
if m1 == m2:
    print("PDFs are identical")
else:
    print("PDFs are not identical")

