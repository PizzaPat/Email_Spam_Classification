#Multinomial Naive Bayes
import classifier
training_file = "../spam_train.txt"
testing_file = "../spam_test.txt"

classifier.email_spam_classifier(training_file, testing_file)
