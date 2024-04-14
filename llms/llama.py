from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline


class LLamaModel:
    def __init__(self, model_name="Maykeye/TinyLLama-v0"):
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        self.generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

    def generate_response(self, prompt):
        result = self.generator(prompt, max_length=150, num_return_sequences=1)
        return result[0]["generated_text"].strip()
