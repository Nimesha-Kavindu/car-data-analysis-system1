#task1
def read_data(filename):
    result = []
    with open(filename, 'r') as file:
        for line in file:
            
            result.append(line.strip().split(','))
    return result

# test task 1
print('.....................Task 1 resualt................')
data = read_data('cars_data.csv')
print(data[0])

#task 2
def process_data(data):

    data_rows = data[1:]

    idx_brand = data[0].index("Brand")
    idx_price = data[0].index("Price")
    idx_mileage = data[0].index("Mileage")
    idx_enginev = data[0].index("EngineV")
    idx_year = data[0].index("Year")
    idx_enginetype = data[0].index("Engine Type")

    preprocessed_data = []

    for row in data_rows:
        brand = row[idx_brand]
        price = float(row[idx_price])
        mileage = float(row[idx_mileage])
        enginev = float(row[idx_enginev])
        year = int(row[idx_year])
        enginetype = row[idx_enginetype]

        preprocessed_data.append((brand, price, mileage, enginev, year, enginetype))

    return preprocessed_data


#test task2
print('.....................Task 2 resualt................')
preprocessed_data = process_data(data)
print(preprocessed_data[0])

#task3
def filter_data(preprocessed_data):
    brand_name = []
    grouped_data = []

    for row in preprocessed_data:
        brand = row[0]
        if brand not in brand_name:
            brand_name.append(brand)
            grouped_data.append([list(row)])
        else:
            idx_brand = brand_name.index(brand)
            grouped_data[idx_brand].append(list(row))

    return brand_name, grouped_data

#test Task 3
print('.....................Task 3 resualt................')
brand_list, grouped_data = filter_data(preprocessed_data)
print(brand_list)
print(grouped_data[0][0])

#task 4. i) 
def average_stdev_price(grouped_data):
    average_price = []
    stdev_price = []

    for brand in grouped_data:
        price = 0
        prices = []

        for car in brand:
            price += car[1]
            prices.append(car[1])

        avg = round(price / len(brand), 2)
        average_price.append(avg)

        variance = sum((p - avg) ** 2 for p in prices) / len(prices)
        std = round(variance ** 0.5, 2)
        stdev_price.append(std)
        
    return average_price, stdev_price

#task 4. i) test
print('.....................Task 4) i) resualt................')
list_avg_prices,list_stdev_prices = average_stdev_price(grouped_data)
print(list_avg_prices)
print(list_stdev_prices)

#task 4. ii)
def price_range(grouped_data):
    price_range = []

    for brand in grouped_data:
        price = []
        for car in brand:
            if car[4] >= 2000:
                price.append(car[1])

        max_price = max(price)
        min_price = min(price)
        price_range.append(round(max_price - min_price, 2))

    return price_range

#task 4. ii) test
print('.....................Task 4) ii) resualt................')
price_ranges = price_range(grouped_data)
print(price_ranges)

#task 4. iii)
def cosine_similarity_by_brand(grouped_data):
    similarity = []

    for brand in grouped_data:
        price = []
        engine_vol = []

        for car in brand:
            if car[5] == 'Petrol':
                price.append(car[1])
                engine_vol.append(car[3])

        sum_of_squares_price = 0
        for p in price:
            sum_of_squares_price += p ** 2
        magnitude_price = sum_of_squares_price ** 0.5

        sum_of_squares_engine = 0
        for e in engine_vol:
            sum_of_squares_engine += e ** 2
        magnitude_engine = sum_of_squares_engine ** 0.5

        dot_product = 0
        for p, e in zip(price, engine_vol):
            dot_product += p * e

        if magnitude_price != 0 and magnitude_engine != 0:
            similarity.append(round(dot_product / (magnitude_price * magnitude_engine), 2))
        else:
            similarity.append(0)
        
    return similarity

#task 4. iii) test
print('.....................Task 4) iii) resualt................')
cosine_similarities = cosine_similarity_by_brand(grouped_data)
print(cosine_similarities)

#task 4. iv)

def average_price_engine_types(grouped_data):
    petrol_prices = []
    diesel_prices = []
    gas_other_prices = []

    for brand in grouped_data:
        for car in brand:
            mileage = car[2]
            price = car[1]
            engine_type = car[5]

            if mileage < 100:
                if engine_type == "Petrol":
                    petrol_prices.append(price)
                elif engine_type == "Diesel":
                    diesel_prices.append(price)
                elif engine_type == "Gas" or engine_type == "Other":
                    gas_other_prices.append(price)

    avg_petrol = sum(petrol_prices)/len(petrol_prices) if len(petrol_prices) != 0 else 0
    avg_diesel = sum(diesel_prices)/len(diesel_prices) if len(diesel_prices) != 0 else 0
    avg_gas_other = sum(gas_other_prices)/len(gas_other_prices) if len(gas_other_prices) != 0 else 0

    return [round(avg_petrol, 2), round(avg_diesel, 2), round(avg_gas_other, 2)]

#task 4. iv) test
print('.....................Task 4) iv) resualt................')
average_price_engines = average_price_engine_types(grouped_data)
print(average_price_engines)

#task 4. v)
def brand_engine_vol(grouped_data, brand_list):
    brand_avg_vol = []

    for i in range(len(brand_list)):
        brand_name = brand_list[i]
        brand_cars = grouped_data[i]

        volume_sum = 0
        for car in brand_cars:
            volume_sum += car[3]

        avg_volume = volume_sum / len(brand_cars)
        brand_avg_vol.append((brand_name, round(avg_volume, 2)))

    return brand_avg_vol

#task 4. v) test
print('.....................Task 4) v) resualt................')
avg_engine_volumes = brand_engine_vol(grouped_data, brand_list)
print(avg_engine_volumes)

#task 5
def affordability_prediction(grouped_data, threshold1=2.6, threshold2=100):
    actual_list = []
    predicted_list = []

    for brand in grouped_data:
        for car in brand:
            price = car[1]
            mileage = car[2]
            engine_vol = car[3]


            if price <= 15000:
                actual_list.append("Yes")
            else:
                actual_list.append("No")


            if engine_vol < threshold1 and mileage > threshold2:
                predicted_list.append("Yes")
            else:
                predicted_list.append("No")

    return actual_list, predicted_list

#task 5 test
print('.....................Task 5) resualt................')
actual, predicted = affordability_prediction(grouped_data)
print(len(actual), len(predicted))
print(actual[0], predicted[0])

#task 6
def result_analysis(actual, predicted):
    TP = FP = TN = FN = 0 

    for a, p in zip(actual, predicted):
        if a == "Yes" and p == "Yes":
            TP += 1
        elif a == "No" and p == "Yes":
            FP += 1
        elif a == "Yes" and p == "No":
            FN += 1
        elif a == "No" and p == "No":
            TN += 1

    accuracy = (TP + TN) / (TP + FP + TN + FN) if (TP + FP + TN + FN) != 0 else 0
    precision = TP / (TP + FP) if (TP + FP) != 0 else 0
    recall = TP / (TP + FN) if (TP + FN) != 0 else 0
    f1_score = 2 * precision * recall / (precision + recall) if (precision + recall) != 0 else 0

    print(f"Accuracy: {round(accuracy,2)}")
    print(f"Precision: {round(precision,2)}")
    print(f"Recall: {round(recall,2)}")
    print(f"F1 Score: {round(f1_score,2)}")

#task 6 test
print('.....................Task 6) resualt................')
result_analysis(actual, predicted)



