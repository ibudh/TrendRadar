import re
import os

files = [
    'trendradar/notification/splitter.py',
    'trendradar/notification/renderer.py',
    'trendradar/report/formatter.py',
    'trendradar/report/helpers.py'
]

# 更加鲁棒的正则，匹配任何 <font ...> 和 </font> 标签
pattern_start = re.compile(r'<font[^>]*>')
pattern_end = re.compile(r'</font>')

for file_path in files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 移除所有 font 标签
        new_content = pattern_start.sub('', content)
        new_content = pattern_end.sub('', new_content)
        
        # 移除 strong 标签
        new_content = new_content.replace('<strong>', '**').replace('</strong>', '**')
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed: {file_path}")
        else:
            print(f"No changes needed for: {file_path}")
