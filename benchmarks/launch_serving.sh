python benchmark_serving.py \
    --host "192.168.0.91" \
    --tokenizer ../../LLAMA2/model/llama-2-7b-chat-hf \
    --port 3090 \
    --dataset "./ShareGPT_V3_unfiltered_cleaned_split.json" \
    --request-rate 7 