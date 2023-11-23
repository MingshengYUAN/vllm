CUDA_VISIBLE_DEVICES=2 python api_server_redis_cluster.py \
    --port 3098 \
    --model ../../../LLAMA2/model/llama-2-7b-chat-hf \
    --max-num-batched-tokens 8000 \
    --dtype half \
    --tensor-parallel-size 1

