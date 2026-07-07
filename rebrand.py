import io
p = "libs/hbb_common/src/config.rs"
s = io.open(p, encoding="utf-8").read()
old = 'APP_NAME: RwLock<String> = RwLock::new("RustDesk"'
new = 'APP_NAME: RwLock<String> = RwLock::new("rkzdesk"'
if old in s:
    s = s.replace(old, new)
    io.open(p, "w", encoding="utf-8", newline="").write(s)
    print("REBRAND: APP_NAME -> rkzdesk (applied)")
else:
    print("REBRAND: PATTERN NOT FOUND! app name line:")
import re
m = re.search(r".*ref APP_NAME.*", io.open(p, encoding="utf-8").read())
print("  ", m.group(0) if m else "(no APP_NAME line)")
print("REBRAND: rkzdesk present now =", "rkzdesk" in io.open(p, encoding="utf-8").read())
