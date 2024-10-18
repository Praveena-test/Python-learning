from itertools import combinations

search_text = "Search_text"
domains = ['Vision', 'Audio', 'NLP']
categories = ['Segmentation', 'Classification', 'PD', 'OD']
licenses = ['A', 'CG', 'CC', 'CL']
filesizes = ['<100MB', '>100MB till <500MB', '>500MB till <1GB', '>1GB']

# Combine all filters into a list
filters = [domains, categories, licenses, filesizes]

# To store test cases
test_cases = []

# Single filter
for domain in domains:
    test_cases.append(f"{search_text} with {domain}")
for category in categories:
    test_cases.append(f"{search_text} with {category}")
for license in licenses:
    test_cases.append(f"{search_text} with {license}")
for filesize in filesizes:
    test_cases.append(f"{search_text} with {filesize}")

# Combinations of two filters
for combo in combinations([*domains, *categories, *licenses, *filesizes], 2):
    test_cases.append(f"{search_text} with {', '.join(combo)}")

# Combinations of three filters
for combo in combinations([*domains, *categories, *licenses, *filesizes], 3):
    test_cases.append(f"{search_text} with {', '.join(combo)}")

# All filters together
all_filters = domains + categories + licenses + filesizes
test_cases.append(f"{search_text} with {', '.join(all_filters)}")

# Print all test cases
for case in test_cases:
    print(case)
