import os
from use_qwen import use_qwen

folder_path = r'C:\Users\admin\Documents\amps\amps\mathematica'
folders = [f for f in os.listdir(folder_path)
           if os.path.isdir(os.path.join(folder_path, f)) and not f.startswith('.')]

for folder in folders:
    subfolder_path = os.path.join(folder_path, folder)
    subfolders = [f for f in os.listdir(subfolder_path)
                  if os.path.isdir(os.path.join(subfolder_path, f)) and not f.startswith('.')]
    for subfolder in subfolders:
        datas = os.listdir(folder_path + f"\\{folder}\\{subfolder}")
        for data in datas:
            with open(folder_path + f"\\{folder}\\{subfolder}\\{data}", "r", encoding="utf-8") as file:
                text = file.read().replace("\n", "")
                prompt = f"Rewrite this text into the following format: First, based on the given text, write a prompt for the language model describing what the user wants to do. Then write \n and a line of dashes (-----). Next, based on the given text, write reasoning for the model on how to arrive at the correct answer. Then write \n and a line of dashes (-----). After that, write the input data, which the model will receive as input, based on the given text. Then write \n and a line of dashes (-----). Finally, write the final result and justify it based on the given text. Don't write anything superfluous. Here is the text itself: {text}"
                answer = use_qwen(prompt)
                d, k, q, v = answer.split("-----")
                os.makedirs(f"ThinkerAIDataset/{subfolder}_{data[:-4]}", exist_ok=True)
                with open(f"ThinkerAIDataset/{subfolder}_{data[:-4]}/d.txt", "w", encoding="utf-8") as f1:
                    f1.write(d)
                with open(f"ThinkerAIDataset/{subfolder}_{data[:-4]}/q.txt", "w", encoding="utf-8") as f2:
                    f2.write(q)
                with open(f"ThinkerAIDataset/{subfolder}_{data[:-4]}/k.txt", "w", encoding="utf-8") as f3:
                    f3.write(k)
                with open(f"ThinkerAIDataset/{subfolder}_{data[:-4]}/v.txt", "w", encoding="utf-8") as f4:
                    f4.write(v)
                print(f"{subfolder}_{data}")
                print("----------------------------------")
                print("\n")
print("Ok")
# wsl -d Ubuntu
# ollama serve