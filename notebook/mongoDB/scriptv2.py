import openfoodfacts
import tarfile

openfoodfacts.utils.download_data()

print("File downloaded!")

tar = tarfile.open("openfoodfacts-mongodbdump.tar.gz", "r:gz")
print("Extracting starting!")
tar.extractall()
print("Extracting finished!")
tar.close()
