import json
import csv

with open('data/output.tsv', mode='w') as output_file:
    output_writer = csv.writer(output_file, delimiter='\t')
    with open('data/dev-v1.1.json') as file:
        data = json.load(file)
        for root in data['data']:
            # for title in root['title']:
            title = root['title']
            print(title.replace("_", "").lower())
                # for questions in paragraph['qas']:
                #     question = questions['question']
                #     answers = questions['answers']
                #     answersText = []
                #     for answer in answers:
                #         answersText.append(answer['text'])
                #     output_writer.writerow([question] + answersText)
        print('**********************************************************************')



# with open('data/wiki.mg4j') as wiki:
#     data = csv.reader(wiki, delimiter='\t')
#     for t in data:
#         print(t)



# with open('data/output.tsv', mode='w') as output_file:
#     output_writer = csv.writer(output_file, delimiter='\t')
#     with open('data/dev-v1.1.json') as file:
#         data = json.load(file)
#         for root in data['data']:
#             for paragraph in root['paragraphs']:
#                 print(paragraph['context'])
#                 # print(paragraph['qas'])
#                 for questions in paragraph['qas']:
#                     question = questions['question']
#                     answers = questions['answers']
#                     answersText = []
#                     for answer in answers:
#                         answersText.append(answer['text'])
#                     output_writer.writerow([question] + answersText)
#         print('**********************************************************************')
