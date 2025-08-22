import openai

class OptionalLLM:
    def __init__(self, api_key=None):
        self.api_key = api_key or "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"
        openai.api_key = self.api_key

    def generate(self, prompt: str, max_tokens: int = 200) -> str:
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=0.7,
            )
            return response.choices[0].text.strip()
        except Exception:
            # fallback dummy output
            return "AI response (offline mode)."
