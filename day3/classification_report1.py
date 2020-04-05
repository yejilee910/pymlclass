# classification_report


# confusion_matrix(y_true, y_pred)
# accuracy_score(y_true, y_pred)
# precision_score(y_true, y_pred)
# recall_score(y_true, y_pred)
# fbeta_score(y_true, y_pred, beta)
# f1_score(y_true, y_pred)
# classfication_report(y_true, y_pred)
# roc_curve
# auc


from sklearn.metrics import confusion_matrix

# 분류결과표(Confusion Matrix)
# y_true = [2, 0, 2, 2, 0, 1]
# y_pred = [0, 0, 2, 2, 0, 2]
y_true = [2, 0, 2, 1, 0, 1, 3, 1, 0, 2, 3, 3]
y_pred = [3, 0, 2, 2, 0, 2, 1, 2, 0, 3, 3, 0]

result = confusion_matrix(y_true, y_pred)
print(result)
result = confusion_matrix(y_true, y_pred, labels=[2, 3])
print("new")
print(result)
