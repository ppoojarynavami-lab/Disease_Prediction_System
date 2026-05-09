def get_recommendation(disease_name):

    # ================= LIVER ================= #

    if disease_name == "Liver":

        return {
            "Disease": "Liver Disease Detected",

            "Diet": [
                "Eat fruits like apple and papaya",
                "Green vegetables",
                "Drink plenty of water",
                "Whole grains"
            ],

            "Avoid": [
                "Alcohol",
                "Fried foods",
                "Junk food",
                "Too much salt"
            ],

            "Routine": [
                "Wake up early",
                "Sleep before 10:30 PM",
                "Light exercise daily",
                "Avoid stress"
            ]
        }

    # ================= DIABETES ================= #

    elif disease_name == "Diabetes":

        return {
            "Disease": "Diabetes Detected",

            "Diet": [
                "Brown rice",
                "Fiber rich foods",
                "Vegetables",
                "Sugar-free foods"
            ],

            "Avoid": [
                "Sugar",
                "Soft drinks",
                "Sweets",
                "Junk food"
            ],

            "Routine": [
                "Walk daily",
                "Exercise regularly",
                "Maintain healthy sleep"
            ]
        }

    # ================= THYROID ================= #

    elif disease_name == "Thyroid":

        return {
            "Disease": "Thyroid Disease Detected",

            "Diet": [
                "Iodine rich foods",
                "Eggs",
                "Fruits",
                "Healthy vegetables"
            ],

            "Avoid": [
                "Processed foods",
                "Excess soy",
                "Junk food"
            ],

            "Routine": [
                "Regular sleep",
                "Daily exercise",
                "Stress management"
            ]
        }

    # ================= HEALTHY ================= #

    else:

        return {
            "Disease": "No Disease Detected",

            "Diet": [
                "Maintain balanced diet",
                "Eat healthy foods",
                "Drink enough water"
            ],

            "Avoid": [
                "Too much junk food",
                "Smoking",
                "Alcohol"
            ],

            "Routine": [
                "Exercise regularly",
                "Maintain good sleep",
                "Stay active"
            ]
        }