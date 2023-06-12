import time
from pypresence import Presence

state_txt = "Sample State"
client_id = '994223622170357761'
RPC = Presence(client_id)
RPC.connect()

RPC.update(
    state=state_txt,  # State text from the variable
    details="Sample Details",
    large_image="large_image_key",
    large_text="Sample Large Text",
    small_image="small_image_key",
    small_text="Sample Small Text",
    start=int(time.time()),
    party_id="party123",
    buttons=[{"label": "Button 1", "url": "https://example.com"}, {"label": "Button 2", "url": "https://example.com"}]
)

while True:
    time.sleep(15)
