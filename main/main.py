from collections import Counter

def analyze_feedback(feedback_list):
    if not feedback_list:
        return {
            'Most Frequent Positive Words': [],
            'Most Frequent Negative Words': [],
            'Overall Sentiment Score': 0,
            'Sentiment Report': 'Positive to Negative Ratio = N/A'
        }

    positive_words = set(['good', 'excellent', 'recommended', 'quick', 'highly'])
    negative_words = set(['terrible', 'bad', 'slow', 'poor'])

    positive_counts = Counter()
    negative_counts = Counter()

    for feedback in feedback_list:
        words = [word.lower().strip('.,?!') for word in feedback.split()]
        positive_counts.update([word for word in words if word in positive_words])
        negative_counts.update([word for word in words if word in negative_words])

    most_frequent_positive_words = [word for word, count in positive_counts.most_common()]
    most_frequent_negative_words = [word for word, count in negative_counts.most_common()]

    overall_sentiment_score = sum(positive_counts[word] for word in positive_words) - sum(negative_counts[word] for word in negative_words)

    total_words = sum(len(feedback.split()) for feedback in feedback_list)

    if total_words == 0:
        return {
            'Most Frequent Positive Words': most_frequent_positive_words,
            'Most Frequent Negative Words': most_frequent_negative_words,
            'Overall Sentiment Score': 0,
            'Sentiment Report': 'Positive to Negative Ratio = N/A'
        }

    positive_count = sum(positive_counts[word] for word in positive_words)
    negative_count = sum(negative_counts[word] for word in negative_words)
    positive_to_negative_ratio = positive_count / max(1, negative_count)

    return {
        'Most Frequent Positive Words': most_frequent_positive_words,
        'Most Frequent Negative Words': most_frequent_negative_words,
        'Overall Sentiment Score': overall_sentiment_score,
        'Sentiment Report': f'Positive to Negative Ratio = {positive_to_negative_ratio:.2f}:1'
    }


# Caso 1
feedback_list_1 = [
    "The service was excellent! Highly recommended.",
    "I had a terrible experience with the product quality.",
    "Good customer support and quick resolution.",
    "Very bad customer support and slow attention.",
    "Poor packaging and delivery service."
]

result_1 = analyze_feedback(feedback_list_1)
print("Caso 1:")
print(result_1)
print("\n---\n")

# Caso 2
feedback_list_2 = [
    "This is a good product.",
    "Excellent service!",
    "Satisfied with my purchase."
]

result_2 = analyze_feedback(feedback_list_2)
print("Caso 2:")
print(result_2)
print("\n---\n")

# Caso 3
feedback_list_3 = [
    "The service was bad.",
    "Poor customer experience.",
    "Terrible quality product."
]

result_3 = analyze_feedback(feedback_list_3)
print("Caso 3:")
print(result_3)
print("\n---\n")
