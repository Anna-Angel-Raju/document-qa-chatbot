
evaluation_dataset = [

    # --------------------------------------------------
    # DIRECT FACTUAL QUESTIONS
    # --------------------------------------------------

    {
        "question": "What is the remaining mortgage balance?",
        "expected": "342,600",
        "category": "Direct"
    },

    {
        "question": "What is the monthly mortgage payment?",
        "expected": "2,180",
        "category": "Direct"
    },

    {
        "question": "What is the interest rate on the mortgage?",
        "expected": "5.35",
        "category": "Direct"
    },

    {
        "question": "How much remains on the car loan?",
        "expected": "11,400",
        "category": "Direct"
    },

    {
        "question": "What is the monthly car loan payment?",
        "expected": "365",
        "category": "Direct"
    },

    {
        "question": "How much is currently in the emergency fund?",
        "expected": "15,000",
        "category": "Direct"
    },

    {
        "question": "What is the target for the emergency fund?",
        "expected": "24,000",
        "category": "Direct"
    },

    {
        "question": "How much is currently in the brokerage account?",
        "expected": "58,300",
        "category": "Direct"
    },


    # --------------------------------------------------
    # PARAPHRASED QUESTIONS
    # --------------------------------------------------

    {
        "question": "How much does the household pay every month toward the home loan?",
        "expected": "2,180",
        "category": "Paraphrased"
    },

    {
        "question": "What amount has been set aside as the household's financial safety cushion?",
        "expected": "15,000",
        "category": "Paraphrased"
    },

    {
        "question": "What sum has been accumulated for repairing the house?",
        "expected": "6,200",
        "category": "Paraphrased"
    },

    {
        "question": "How much money has been put away for the eventual replacement of Priya's car?",
        "expected": "4,800",
        "category": "Paraphrased"
    },

    {
        "question": "What is the current value of the household's taxable investment account?",
        "expected": "58,300",
        "category": "Paraphrased"
    },


    # --------------------------------------------------
    # CONCEPTUAL QUESTIONS
    # --------------------------------------------------

    {
        "question": "Why does the household keep several savings accounts instead of putting all the money into one account?",
        "expected": "separate goals",
        "category": "Conceptual"
    },

    {
        "question": "Why is the emergency fund kept separate from the home repair fund?",
        "expected": "emergencies",
        "category": "Conceptual"
    },

    {
        "question": "Why do Daniel and Priya consider the car loan more urgent than the mortgage?",
        "expected": "higher rate",
        "category": "Conceptual"
    },

    {
        "question": "Why don't they consider their brokerage account to be emergency savings?",
        "expected": "market",
        "category": "Conceptual"
    },

    {
        "question": "Why is the vacation fund considered more flexible than the vehicle fund?",
        "expected": "vacation can be postponed",
        "category": "Conceptual"
    },


    # --------------------------------------------------
    # COMPARISON QUESTIONS
    # --------------------------------------------------

    {
        "question": "Which has the higher interest rate, the mortgage or the car loan?",
        "expected": "car loan",
        "category": "Comparison"
    },

    {
        "question": "How does the purpose of the emergency fund differ from the home repair fund?",
        "expected": "emergency fund",
        "category": "Comparison"
    },

    {
        "question": "How are the brokerage account and cryptocurrency holdings treated differently?",
        "expected": "cryptocurrency",
        "category": "Comparison"
    },

    {
        "question": "Which is considered more urgent, replacing the car or taking the vacation?",
        "expected": "vehicle",
        "category": "Comparison"
    },


    # --------------------------------------------------
    # MULTI-HOP QUESTIONS
    # --------------------------------------------------

    {
        "question": "Why do they prioritize paying off the car loan before making extra mortgage payments?",
        "expected": "car loan",
        "category": "Multi-hop"
    },

    {
        "question": "What financial priority comes after finishing the car loan?",
        "expected": "emergency fund",
        "category": "Multi-hop"
    },

    {
        "question": "Why does the household continue retirement contributions even while dealing with shorter-term goals?",
        "expected": "long-term",
        "category": "Multi-hop"
    },


    # --------------------------------------------------
    # MISSING INFORMATION / HALLUCINATION TESTS
    # --------------------------------------------------

    {
        "question": "What is the name of the institution that currently services the mortgage?",
        "expected": "I couldn't find this information",
        "category": "Missing Information"
    },

    {
        "question": "What is the current balance of the college fund?",
        "expected": "I couldn't find this information",
        "category": "Missing Information"
    },

    {
        "question": "What specific car model does Priya plan to buy?",
        "expected": "I couldn't find this information",
        "category": "Missing Information"
    },

    {
        "question": "What is their planned vacation destination?",
        "expected": "I couldn't find this information",
        "category": "Missing Information"
    },

    {
        "question": "What medications are Daniel and Priya currently taking?",
        "expected": "I couldn't find this information",
        "category": "Missing Information"
    },


    # --------------------------------------------------
    # NUMERICAL / CALCULATION QUESTIONS
    # --------------------------------------------------

    {
        "question": "How much more money is needed to reach the emergency fund target?",
        "expected": "9,000",
        "category": "Calculation"
    },

    {
        "question": "How much more is needed to reach the home repair fund target?",
        "expected": "3,800",
        "category": "Calculation"
    },

    {
        "question": "How much more is needed to reach the vacation fund target?",
        "expected": "1,850",
        "category": "Calculation"
    },

    {
        "question": "How much more is needed for the vehicle savings account to reach its target?",
        "expected": "7,200",
        "category": "Calculation"
    }
]
