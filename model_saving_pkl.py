import pickle
file_name="give_the_fielname_with_extension.pkl"
model_name="model_which your trained"
#for code dumping using pickle
pickle.dump(model_name,open("filename","wb"))
#to load the model once again using the pickle file
loaded_model=pickle.load(open("filename","rb"))
#Now use that model for predictions
prediction=loaded_model.predict(x_test)
