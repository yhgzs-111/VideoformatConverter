import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import ffmpeg

class VideoConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("视频格式无损转换工具")

        self.source_label = tk.Label(root, text="选择源文件:")
        self.source_label.pack()

        self.source_entry = tk.Entry(root, width=50)
        self.source_entry.pack()

        self.browse_button = tk.Button(root, text="浏览", command=self.browse_source)
        self.browse_button.pack()

        self.format_label = tk.Label(root, text="输入目标格式:")
        self.format_label.pack()

        self.format_entry = tk.Entry(root, width=10)
        self.format_entry.pack()

        self.destination_label = tk.Label(root, text="选择输出文件夹:")
        self.destination_label.pack()

        self.destination_entry = tk.Entry(root, width=50)
        self.destination_entry.pack()

        self.browse_dest_button = tk.Button(root, text="浏览", command=self.browse_destination)
        self.browse_dest_button.pack()

        self.convert_button = tk.Button(root, text="无损转换", command=self.convert)
        self.convert_button.pack()

    def browse_source(self):
        file_path = filedialog.askopenfilename(filetypes=[])
        self.source_entry.delete(0, tk.END)
        self.source_entry.insert(0, file_path)

    def browse_destination(self):
        folder_path = filedialog.askdirectory()
        self.destination_entry.delete(0, tk.END)
        self.destination_entry.insert(0, folder_path)

    def convert(self):
        source_file = self.source_entry.get()
        destination_folder = self.destination_entry.get()
        output_format = self.format_entry.get()

        if not source_file or not destination_folder or not output_format:
            return

        output_file = os.path.join(destination_folder, "converted" + output_format)

        try:
            process = ffmpeg.input(source_file).output(output_file, c="copy").run(capture_stdout=True, capture_stderr=True)
            messagebox.showinfo("成功", "无损转换完成！")
        except Exception as e:
            messagebox.showerror("错误", "转换失败，未知原因")
            if os.path.exists(output_file):
                os.remove(output_file)

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoConverterApp(root)
    root.mainloop()
