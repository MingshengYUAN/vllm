import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import time
import numpy as np

concurrency = 50
start_time = time.time()
all_len = 0
len_max = 0
len_min = 10000
flag = 0

system_prompt = f"You are a large language model named AraMUS developed by TONOMUS, " \
                    f"NEOM to chat with the users. Please respond to users professionally" \
                    f"and honestly. Only respond to the last instruction. " \

base_qa_parirs_prompt = "AraMUS is a state-of-the-art family of Arabic NLP models developed to efficiently process Arabic Language while taking cultural \
              context into account and enable KSA to be in control of Data & AI in alignment with national strategy. AraMUS is led by Asaad \
              Alghamdi. NEOM is a region in the northwest of the Kingdom of Saudi Arabia. NEOM means ‘new future’ and with more than 2800 staff, \
              from 86 countries, already living and working here onsite, it has already become a home for people who dream big and want to be part \
              of building a new economic model for the country and the world. Tonomus is the first company to be established as a full-fledged \
              subsidiary of NEOM. Tonomus is a world-leading technology enterprise powering the world's first ecosystem of cognitive technologies \
              at NEOM. Safana is a state-of-the-art omnipresent conversational digital human to represent NEOM. Safana is powered by ​the world's \
              first large-scale pre-trained Arabic NLP model. Safana is led by Alya Alqarni. Coglens is a world-leading technology enterprise \
              powering the world's first ecosystem of cognitive technologies at NEOM. Coglens is led by Dr. Majid Al-Sayegh."

user_input = "Can you tell me what is Aramus and NEOM?"

input_text = f"""
    <<SYS>>
    {system_prompt.strip()}
    <</SYS>>

    {base_qa_parirs_prompt.strip()}
    [INST] {user_input.strip()} [/INST]"""

def send_request(url):
    global input_text
    global all_len
    global flag
    global len_max
    global len_min
    # post_dict = {"prompt": input_text, "stream": True, "max_tokens": 512, "top_p": 0.9, "frequency_penalty": 0, "use_beam_search": False}
    post_dict = {"chat_input": "Who are you?", "messages": "xxxxx", "user_info": "xxxxx", "id": "1c7ecc18-9f04-4261-a566-c47dfeda25f5", "msg_id": "a91b38487b174b9d8c3fc34e39f767a0"}
    headers = {"Content-Type": "application/json"}
    start = time.time()
    response = requests.post(url, json.dumps(post_dict), headers=headers)
    tmp = eval(response.text)
    time_end = float(tmp['time'])
    
    return float(time.time() - start)
    # return response.status_code
# 05gpu 1card with llama 7b stream para
# url = 'http://37.224.68.132:27090/generate'

# 06gpu 4cards with llama 7b stream para
# url = 'http://37.224.68.132:27190/generate'

# 06GPU 1card with llama 7b stream redis
url = 'http://37.224.68.132:27199/generate'

# url = 'http://37.224.68.132:27195/generate'
urls = []
results = 0.0
max_result = 0.0
min_result = 100000.0
for i in range(concurrency):
    urls.append(url)
with ThreadPoolExecutor(max_workers=7) as executor:
    all_task = [executor.submit(send_request, url) for url in urls]
    for future in as_completed(all_task):
        results += future.result()
        max_result = max(future.result(), max_result)
        min_result = min(future.result(), min_result)
    # results = executor.map(send_request, urls)


        # print(f"Response : {response}")
all_time = float(time.time() - start_time)
print(f"total count : {concurrency}")
print(f"All_exec_time : {results}")
print(f"max_exec_time : {max_result}, ")
print(f"min_exec_time : {min_result}")

print(f"Average time : {results / concurrency}")
print(f"All time : {all_time}")
# print(f"Avg len : {all_len / concurrency}")
# print(f"Max len : {len_max}")
# print(f"Min len : {len_min}")