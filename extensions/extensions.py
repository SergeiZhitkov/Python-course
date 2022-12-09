

def main():
    file = input("File name: ").strip().lower()
    print(file_extension(file))



def file_extension(f):
    suffix = ""
    extensions = {
        ".gif" : "image/gif",
        ".jpg" : "image/jpeg",
        ".jpeg" : "image/jpeg",
        ".png" : "image/png",
        ".pdf" : "application/pdf",
        ".txt" : "text/plain",
        ".zip" : "application/zip",
       }
    if f.endswith((".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip")):
        f = f.replace("jpeg", "jpg")
        for letter in f[-4:]:
            suffix = suffix + letter
        return extensions[suffix]
    return "application/octet-stream"




if __name__ == "__main__":
    main()