mkdir Data

# download images
curl -o Data/images.tar http://vision.stanford.edu/aditya86/ImageNetDogs/images.tar
tar xfz Data/images.tar -C Data
rm Data/images.tar

# download annotations
curl -o annotations.tar http://vision.stanford.edu/aditya86/ImageNetDogs/annotation.tar
tar xfz Data/annotations.tar -C Data
rm Data/annotations.tar