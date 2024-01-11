from llama_cpp import Llama
from huggingface_hub import hf_hub_download


def down_model():
    model_name_or_path = "TheBloke/Llama-2-13B-chat-GGML"
    model_basename = "llama-2-13b-chat.ggmlv3.q5_1.bin" 
    # the model is in bin format   
    model_path = hf_hub_download(repo_id=model_name_or_path, filename=model_basename)
    return model_path
def load_model():
    lcpp_llm = None
    lcpp_llm = Llama(
        model_path='./model',
        n_threads=1,
        n_batch=1,
        n_gpu_layers=1
    )
    return lcpp_llm

def query(prompt,lcpp_llm,SYSTEM_PROMPT='eres una asistente personal que que busca ayudar lo mejor posible'):
    prompt_template = f'''
    SYSTEM: {SYSTEM_PROMPT}
    USER: {prompt}
    ASSISTANT:
    '''
    response=lcpp_llm(prompt=prompt_template, max_tokens=256, temperature=0.3, top_p=0.95,repeat_penalty=1.2, top_k=150)

    print(response('choices')[0]('text'))


down_model()