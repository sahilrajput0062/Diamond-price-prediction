def predict_price(carat, depth, table, x, y, z, cut, color, clarity):
    # Create a DataFrame with the categorical features
    categorical_data = pd.DataFrame({'cut': [cut.lower()], 'color': [color.lower()], 'clarity': [clarity.lower()]})

    try:
        # Use LabelEncoder for ordinal categorical features
        categorical_data['cut'] = __cut_values.index(categorical_data['cut'][0])
        categorical_data['color'] = __color_values.index(categorical_data['color'][0])
        categorical_data['clarity'] = __clarity_values.index(categorical_data['clarity'][0])
    except ValueError as e:
        print("Error during LabelEncoding:", e)
        print("cut_values:", __cut_values)
        print("color_values:", __color_values)
        print("clarity_values:", __clarity_values)

    # Ensure the features are in the same order as during training
    input_features = np.array([[carat, depth, table, x, y, z, categorical_data['cut'][0], categorical_data['color'][0], categorical_data['clarity'][0]]])

    try:
        predicted_price = round(__model.predict(input_features)[0], 2)
        return predicted_price
    except Exception as e:
        print("Error during prediction:", e)
        return None