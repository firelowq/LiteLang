import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    path = filedialog.askopenfilename(filetypes=[("LiteLang files", "*.lite")])
    if path:
        with open(path, "r", encoding="utf-8") as file:
            text.delete("1.0", tk.END)
            text.insert(tk.END, file.read())
        root.title(f"LiteLang Editor - {path}")
        root.file_path = path

def save_file():
    if hasattr(root, 'file_path'):
        with open(root.file_path, "w", encoding="utf-8") as file:
            file.write(text.get("1.0", tk.END))
    else:
        save_as()

def save_as():
    path = filedialog.asksaveasfilename(defaultextension=".lite", filetypes=[("LiteLang files", "*.lite")])
    if path:
        with open(path, "w", encoding="utf-8") as file:
            file.write(text.get("1.0", tk.END))
        root.title(f"LiteLang Editor - {path}")
        root.file_path = path

def run_litelang_code(code):
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "LiteLang Demo\nType \"help\" for more information.\n\n", "demo")
    
    for line in code.splitlines():
        line = line.strip()
        if line.startswith("show "):
            expr = line[5:].strip()
            try:
                # Burada güvenlik önlemi yok, sadece demo
                result = eval(expr)
                output_text.insert(tk.END, str(result) + "\n", "output")
            except Exception as e:
                output_text.insert(tk.END, f"Hata: {e}\n", "error")
        elif line == "":
            continue
        else:
            output_text.insert(tk.END, f"Anlaşılmayan komut: {line}\n", "error")

def run_file():
    if not hasattr(root, 'file_path'):
        save_as()
    else:
        save_file()
    if hasattr(root, 'file_path'):
        with open(root.file_path, "r", encoding="utf-8") as f:
            code = f.read()
        run_litelang_code(code)

def evaluate_expression(expr):
    # Örnek basit parser: stringler "" içinde, geri kalan sayılar ve + - * /
    # İlk olarak stringleri koru, onları token yap
    import re
    tokens = []
    pos = 0
    string_pat = re.compile(r'"[^"]*"')
    
    while pos < len(expr):
        m = string_pat.match(expr, pos)
        if m:
            tokens.append(m.group())
            pos = m.end()
        else:
            if expr[pos].isspace():
                pos +=1
            else:
                tokens.append(expr[pos])
                pos +=1

    # tokens örn: ['"sonuç: "', '+', '3', '+', '4']

    # şimdi parçaları birleştirip, string ise koru, sayı ise int yap
    parsed = []
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t.startswith('"') and t.endswith('"'):
            parsed.append(t[1:-1])
        elif t in "+-*/":
            parsed.append(t)
        elif t.isdigit():
            parsed.append(int(t))
        else:
            # boşluk vs
            pass
        i += 1

    # basit hesaplama soldan sağa, string + sayı = string concat
    # işlemleri soldan sağa sırayla yaparız
    def apply_op(a, op, b):
        if op == '+':
            if isinstance(a, str) or isinstance(b, str):
                return str(a) + str(b)
            else:
                return a + b
        elif op == '-':
            if isinstance(a, (int,float)) and isinstance(b, (int,float)):
                return a - b
            else:
                raise Exception("Çıkarma işlemi sadece sayılarla yapılır")
        elif op == '*':
            if isinstance(a, (int,float)) and isinstance(b, (int,float)):
                return a * b
            else:
                raise Exception("Çarpma işlemi sadece sayılarla yapılır")
        elif op == '/':
            if isinstance(a, (int,float)) and isinstance(b, (int,float)):
                if b == 0:
                    raise Exception("Sıfıra bölme hatası")
                return a / b
            else:
                raise Exception("Bölme işlemi sadece sayılarla yapılır")
        else:
            raise Exception(f"Bilinmeyen operatör: {op}")

    if not parsed:
        return ""

    result = parsed[0]
    idx = 1
    while idx < len(parsed):
        op = parsed[idx]
        val = parsed[idx+1]
        result = apply_op(result, op, val)
        idx += 2

    return result

root = tk.Tk()
root.title("LiteLang Editor")
root.geometry("800x600")
root.configure(bg="#1e1e1e")

text = tk.Text(root, bg="#1e1e1e", fg="#ffffff", insertbackground="#ffffff", font=("Consolas", 12))
text.pack(expand=True, fill="both")

output_text = tk.Text(root, height=10, bg="#2e2e2e", fg="#00ff00", font=("Consolas", 12))
output_text.pack(fill="x")
output_text.insert(tk.END, "LiteLang Demo\nType \"help\" for more information.\n\n")

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Dosya Aç", command=open_file)
file_menu.add_command(label="Kaydet", command=save_file)
file_menu.add_command(label="Farklı Kaydet", command=save_as)
file_menu.add_separator()

def exit_app():
    if messagebox.askyesno("Kaydet", "Dosya kaydedilsin mi?"):
        save_file()
    root.destroy()

file_menu.add_command(label="Çıkış", command=exit_app)
menu_bar.add_cascade(label="Dosya", menu=file_menu)

run_menu = tk.Menu(menu_bar, tearoff=0)
run_menu.add_command(label="Çalıştır", command=run_file)
menu_bar.add_cascade(label="Çalıştır", menu=run_menu)

root.config(menu=menu_bar)

import sys
import traceback

if __name__ == "__main__":
    try:
        root.mainloop()
    except Exception:
        traceback.print_exc()
        input("HATA OLDU. Devam etmek için Enter'a bas...")

