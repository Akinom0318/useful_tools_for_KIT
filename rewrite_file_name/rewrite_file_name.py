import os

def rename_files():
    # 取得使用者要替換的舊文字與新文字
    old_text = input("請輸入要替換的文字: ")
    new_text = input("請輸入新文字: ")

    # 獲取當前資料夾的路徑
    current_folder = os.getcwd()

    # 遍歷當前資料夾的文件
    for filename in os.listdir(current_folder):
        # 檢查是否為文件，並且文件名包含舊文字
        if os.path.isfile(filename) and old_text in filename:
            # 新文件名：將舊文字替換成新文字
            new_filename = filename.replace(old_text, new_text)
            
            # 重新命名文件
            os.rename(filename, new_filename)
            print(f"已重命名: {filename} -> {new_filename}")

if __name__ == "__main__":
    rename_files()
