# Naive Bayes model
y_pred = nb_classifier.predict(X_test_tfidf)
# Evaluate the Naive Bayes model
print("Naive Bayes Results:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# Naive Bayes with Genetic Algorithm
final_predictions = final_classifier.predict(final_X_test)
# Evaluate the Naive Bayes with Genetic Algorithm
print("\nFinal Model Results with GA-selected features:")
print("Accuracy:", accuracy_score(y_test, final_predictions))
print("Classification Report:")
print(classification_report(y_test, final_predictions))