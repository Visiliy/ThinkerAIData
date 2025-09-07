import ollama


def use_qwen(prompt):
    response = ollama.chat(
        model='qwen3:8b',
        messages=[
            {'role': 'user', 'content': prompt}
        ]
    )
    response = response['message']['content'].split("</think>")[-1]
    response = response.split("\n\n")[-1]
    return response


if __name__ == '__main__':
    print(use_qwen('What is the capital of France?'))