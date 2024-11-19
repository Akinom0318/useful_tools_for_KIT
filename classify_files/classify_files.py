import os
import shutil

def move_files_by_keyword():
    # 讓使用者輸入關鍵字
    keyword = input("請輸入關鍵字: ").strip()
    if not keyword:
        print("關鍵字不能為空！")
        return
    
    # 獲取當前資料夾路徑
    current_folder = os.getcwd()
    
    # 檢查或創建目標資料夾
    target_folder = os.path.join(current_folder, keyword)
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        print(f"已創建資料夾: {target_folder}")
    
    # 遍歷當前資料夾的檔案
    moved_files = 0
    for filename in os.listdir(current_folder):
        file_path = os.path.join(current_folder, filename)
        
        # 檢查是否為檔案，並且檔名包含關鍵字
        if os.path.isfile(file_path) and keyword in filename:
            # 移動檔案到目標資料夾
            shutil.move(file_path, os.path.join(target_folder, filename))
            print(f"已移動檔案: {filename}")
            moved_files += 1
    
    if moved_files == 0:
        print(f"未找到包含關鍵字 '{keyword}' 的檔案。")
    else:
        print(f"完成，總共移動了 {moved_files} 個檔案至資料夾 '{keyword}'。")

if __name__ == "__main__":
    move_files_by_keyword()
