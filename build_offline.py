import json, pathlib

# اقرأ ملف المنتجات (products.json)
with open("products.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# اقرأ القالب (customs-offline-template.html)
tpl = pathlib.Path("customs-offline-template.html").read_text(encoding="utf-8")

# استبدل مكان DB
start = tpl.find("const DB = [")
end   = tpl.find("];", start) + 2
new   = tpl[:start] + "const DB = " + json.dumps(data, ensure_ascii=False) + ";" + tpl[end:]

# احفظ الملف النهائي
pathlib.Path("customs-offline.html").write_text(new, encoding="utf-8")
print("✅ تم تجهيز customs-offline.html النهائي 100%")