import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
import joblib

file_name= r"C:\Users\Zaina\OneDrive - University of Cincinnati\Spring 2023\Senior Design\ml_code\data\archive\themes-lyrics.csv"

# Load the CSV file into a Pandas DataFrame
data = pd.read_csv(file_name, on_bad_lines='skip')
print('Loaded data')

# Split the data into training and testing sets
train_data = data.sample(frac=0.8, random_state=1)
test_data = data.drop(train_data.index)
print('Splitting test-train data')

# Extract the lyrics and themes from the training data
train_lyrics = train_data["lyrics"].tolist()
train_themes = train_data["theme"].tolist()

# Create a bag of words representation of the lyrics
vectorizer = CountVectorizer(stop_words='english')
train_features = vectorizer.fit_transform(train_lyrics)

# Train the SVM classifier
clf = svm.SVC(kernel='linear')
clf.fit(train_features, train_themes)

# Save the trained classifier to disk
joblib.dump(clf, "classifier.joblib")

# Extract the lyrics and themes from the testing data
test_lyrics = test_data["lyrics"].tolist()
test_themes = test_data["theme"].tolist()

# Create a bag of words representation of the testing lyrics
test_features = vectorizer.transform(test_lyrics)

# Use the trained SVM classifier to predict the themes for the testing lyrics
predictions = clf.predict(test_features)

# Print the accuracy of the predictions
correct = 0
for i in range(len(test_themes)):
    if test_themes[i] == predictions[i]:
        correct += 1
accuracy = correct / len(test_themes)
print("Accuracy:", accuracy)