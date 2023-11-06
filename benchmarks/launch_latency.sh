CUDA_VISIBLE_DEVICES=6 python benchmark_latency.py \
    --model ../../LLAMA2/model/llama-2-7b-chat-hf \
    --tensor-parallel-size 1 \
    --input-len 512 \
    --output-len 512 \
    --batch-size 8 \
    --dtype bfloat16