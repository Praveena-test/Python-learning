Search_text = ['audio file']
domains = ['Vision', 'Audio', 'NLP']
categories = ['Segmentation', 'Classification', 'Pose Detection', 'Object Detection']
licenses = ['Apache 2.0', 'GPL3.0', 'CC-BY 4.0', 'Custom License']
filesizes = ['<100MB', '>100MB till <500MB', '>500MB till <1GB', '>1GB']

test_cases = []
for domain in domains:
    for category in categories:
        for license in licenses:
            for filesize in filesizes:
                for search in Search_text:
                    test_cases.append((domain, category, license, filesize))

# Print all test cases
for i, case in enumerate(test_cases, 1):
    print(f"{i}. {case[0]}, {case[1]}, {case[2]}, {case[3]}")
