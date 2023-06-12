import config
import time
from pypresence import Presence
# Read cfg
try:
    with open('main.cfg', 'r') as file:
        # Read all lines from the file
        lines = file.readlines()
# If cfg file not found
except FileNotFoundError:
    # Generate Config
    config.missing_cfg()
    # Retry Reading
    with open('main.cfg', 'r') as file:
        lines = file.readlines()
# Get the third line (index 2, since Python uses zero-based indexing)
line3 = lines[2]  # This Was Client ID
line4 = lines[3]  # State
line5 = lines[4]  # Details
line6 = lines[5]  # Large Image That on Application Bot
line7 = lines[6]  # Large Image Text
line8 = lines[7]  # Small Image That on Application Bot
line9 = lines[8]  # Small Image Text
line10 = lines[9]  # Party id        IDK about this
line11 = lines[10]  # Button 1 Text
line12 = lines[11]  # Button 1 Url
line13 = lines[12]  # Button 2 Text
line14 = lines[13]  # Button 2 Url

client_id_raw = line3.strip()
state_raw = line4.strip()
details_raw = line5.strip()
large_img_raw = line6.strip()
large_imgtext_raw = line7.strip()
small_img_raw = line8.strip()
small_imgtext_raw = line9.strip()
party_raw = line10.strip()
btn1_raw = line11.strip()
btn1url_raw = line12.strip()
btn2_raw = line13.strip()
btn2url_raw = line14.strip()

# Remove Prefix
client_id = client_id_raw.replace("client-id=", "")
state_txt = state_raw.replace("state=", "")
details_txt = details_raw.replace("details=", "")
large_img = large_img_raw.replace("large_image=", "")
large_img_text = large_imgtext_raw.replace("large_text=", "")
small_img = small_img_raw.replace("small_image=", "")
small_img_text = small_imgtext_raw.replace("small_text=", "")
party_id = party_raw.replace("party_id=", "")
button1_txt = btn1_raw.replace("button1=", "")
button1_url = btn1url_raw.replace("button1_link=", "")
button2_txt = btn2_raw.replace("button2=", "")
button2_url = btn2url_raw.replace("button2_link=", "")

print("Using This Settings :")
print(client_id)
print(state_txt)
print(details_txt)
print(large_img)
print(large_img_text)
print(small_img)
print(small_img_text)
print(party_id)
print(button1_txt)
print(button1_url)
print(button2_txt)
print(button2_url)

# This is Discord
RPC = Presence(client_id)
RPC.connect()
RPC.update(
    state=state_txt,
    details=details_txt,
    large_image=large_img,
    large_text=large_img_text,
    small_image=small_img,
    small_text=small_img_text,
    start=int(time.time()),
    party_id=party_id,
    buttons=[{"label": button1_txt, "url": button1_url}, {"label": button2_txt, "url": button2_url}]
)

# Update Every 15 sec
while True:
    time.sleep(15)
