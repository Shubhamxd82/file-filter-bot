class script(object):
    HELP_TXT = """𝙷𝙴𝚈 {}
ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʜᴇʟᴘ ꜰᴏʀ ᴍʏ ᴄᴏᴍᴍᴀɴᴅ."""
    ABOUT_TXT = """<b>✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}</b>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝚅𝙿𝚂
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v4.0.2 [ 𝙱𝙴𝚃𝙰 ]""" 
    SOURCE_TXT = """<b>NOTE:</b>
- <b> bot is a not open source project. 
- contact my Owner</b>

<b>Message:</b>
- <a href=https://t.me/AkshayChand10>Akshay Chand</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Bot have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- movies house Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/AkshayChand10)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """ ★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱 """
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

    START_TXT = """<b>ʜᴀʏ {},

ɪ'ᴍ ⚡️ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ-ꜰɪʟᴛᴇʀ ʙᴏᴛ...
😎 ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ ᴀꜱ ᴀ ᴀᴜᴛᴏ-ꜰɪʟᴛᴇʀ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ....
ɪᴛꜱ ᴇᴀꜱʏ ᴛᴏ ᴜꜱᴇ ᴍᴇ; ᴊᴜꜱᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀꜱ ᴀᴅᴍɪɴ, ᴛʜᴀᴛꜱ ᴀʟʟ, ɪ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇꜱ ᴛʜᴇʀᴇ...😎
⚠️ ᴍᴏʀᴇ ʜᴇʟᴘ ᴄʜᴇᴄᴋ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ</b>"""

    GHHM_TXT = """<b> Repo Developer
<a href=https://t.me/TeamEvamaria>Team Eva Maria</a>

More Features Add 1
Extra Features: 
🔹download songs,
🔹download you tube video,
🔹URL Shortner

<a href=https://t.me/sahid_malik>Sahid Malik</a>

More Features Add 2
🔹Welcome message
🔹Group adding message
🔹Group start message
🔹ShareUs Link Shortner Site 

<a href=https://t.me/AkshayChand10>Akshay Chand</a></b>"""

    GHHN_TXT = """Extra features"""

    MALIK_TXT =  """<b>Donation</b>
   
   <b>Developer is Super Noob..  Just Learning from Official Docs..  Please Donate the developer for Keeping the Service Alive...</b>


⪼ <b>𝐘𝐨𝐮 𝐂𝐚𝐧 𝐃𝐨𝐧𝐚𝐭𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 💳. 

Payment Methods

✮ 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
✮ 𝗣𝗮𝘆𝘁𝗺           
✮ 𝗣𝗵𝗼𝗻𝗲𝗣𝗲     
✮ 𝗣𝗮𝘆𝗣𝗮𝗹
𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐅𝐨𝐫 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨

<a href=https://t.me/AkshayChand10><b>Akshay Chand</b></a>"""
    DINETTE_TXT =  """<b>Donation</b>

   <b>Developer is Super Noob..  Just Learning from Official Docs..  Please Donate the developer for Keeping the Service Alive...</b>


⪼ <b>𝐘𝐨𝐮 𝐂𝐚𝐧 𝐃𝐨𝐧𝐚𝐭𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 💳. 

Payment Methods

✮ 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
✮ 𝗣𝗮𝘆𝘁𝗺           
✮ 𝗣𝗵𝗼𝗻𝗲𝗣𝗲     
✮ 𝗣𝗮𝘆𝗣𝗮𝗹
𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐅𝐨𝐫 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨 

<a href=https://t.me/AkshayChand10><b>Akshay Chand</b></a>"""


    URLSHORT_TXT = """<b>➤ 𝐇𝐞𝐥𝐩: 𝖴𝗋𝗅 𝗌𝗁𝗈𝗋𝗍𝗇𝖾𝗋

𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚜𝚑𝚘𝚛𝚝 𝚊 𝚞𝚛𝚕 

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ /short: 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
/short https://t.me/+veUIdIW2CQ5GU5</b>"""


    URLSHORTN_TXT = """<b>➤ 𝐇𝐞𝐥𝐩: 𝖴𝗋𝗅 𝗌𝗁𝗈𝗋𝗍𝗇𝖾𝗋

𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚜𝚑𝚘𝚛𝚝 𝚊 𝚞𝚛𝚕 

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ /short: 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
/short https://t.me/+veUIdIW25mOGU5</b>"""

    VIDEO_TXT ="""<b>𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝚅𝙸𝙳𝙴𝙾 𝙵𝚁𝙾𝙼 𝚈𝙾𝚄𝚃𝚄𝙱𝙴.

• 𝘜𝘴𝘢𝘨𝘦
𝘠𝘰𝘶 𝘊𝘢𝘯 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘈𝘯𝘺 𝘝𝘪𝘥𝘦𝘰 𝘍𝘳𝘰𝘮 𝘠𝘰𝘶𝘵𝘶𝘣𝘦

𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
• 𝘛𝘺𝘱𝘦 /video or /mp4 𝘈𝘯𝘥 (𝘝𝘪𝘥𝘦𝘰 Link)
• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦:
/𝘮𝘱4 https://youtu.be/Your Link</b>"""

    VIDEOS_TXT ="""<b>𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝚅𝙸𝙳𝙴𝙾 𝙵𝚁𝙾𝙼 𝚈𝙾𝚄𝚃𝚄𝙱𝙴.

• 𝘜𝘴𝘢𝘨𝘦
𝘠𝘰𝘶 𝘊𝘢𝘯 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘈𝘯𝘺 𝘝𝘪𝘥𝘦𝘰 𝘍𝘳𝘰𝘮 𝘠𝘰𝘶𝘵𝘶𝘣𝘦

𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
• 𝘛𝘺𝘱𝘦 /video or /mp4 𝘈𝘯𝘥 (𝘝𝘪𝘥𝘦𝘰 Link)
• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦:
/𝘮𝘱4 https://youtu.be/Your Link</b>"""

    YTTHUMB_TXT = """<b>𝙷𝙴𝙻𝙿𝚂 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙰𝙽𝚈 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝚅𝙸𝙳𝙴𝙾 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻
    
⭕𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
𝘛𝘺𝘱𝘦 /ytthumb 𝘈𝘯𝘥 𝘝𝘪𝘥𝘦𝘰 𝘓𝘪𝘯𝘬

• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦
/ytthumb https://youtu.be/yourlink</b>"""

    SONG_TXT = """<b>𝚂𝙾𝙽𝙶 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙼𝙾𝙳𝚄𝙻𝙴...

𝚂𝙾𝙽𝙶 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙼𝙾𝙳𝚄𝙻𝙴, 𝙵𝙾𝚁 𝚃𝙷𝙾𝚂𝙴 𝚆𝙷𝙾 𝙻𝙾𝚅𝙴 𝙼𝚄𝚂𝙸𝙲. 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙵𝙴𝙰𝚃𝚄𝙴 𝙵𝙾𝚁 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙰𝙽𝚈 𝚂𝙾𝙽𝙶 𝚆𝙸𝚃𝙷 𝚂𝚄𝙿𝙴𝚁 𝙵𝙰𝚂𝚃 𝚂𝙿𝙴𝙴𝙳.𝚆𝙾𝚁𝙺𝚂 𝙾𝙽𝙻𝚈 𝙾𝙽 𝙶𝚁𝙾𝚄𝙿𝚂..

<𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂

››  /song 𝚂𝙾𝙽𝙶 𝙽𝙰𝙼𝙴 

𝚆𝙾𝚁𝙺𝚂 𝙾𝙽𝙻𝚈 𝙾𝙽 𝙶𝚁𝙾𝚄𝙿"""


    FILESTORE_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝐅𝐢𝐥𝐞 𝐒𝐭𝐨𝐫𝐞 𝐌𝐨𝐝𝐮𝐥𝐞../

<b>𝙱𝚈 𝚄𝚂𝙸𝙽𝙶 𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚂𝚃𝙾𝚁𝙴 𝙵𝙸𝙻𝙴𝚂 𝙸𝙽 𝙼𝚈 𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴 𝙰𝙽𝙳 𝙸 𝚆𝙸𝙻𝙻 𝙶𝙸𝚅𝙴 𝚈𝙾𝚄 𝙰 𝙿𝙴𝚁𝙼𝙰𝙽𝙴𝙽𝚃 𝙻𝙸𝙽𝙺  𝚃𝙾 𝙰𝙲𝙲𝙴𝚂𝚂 𝚃𝙷𝙴 𝚂𝙰𝚅𝙴𝙳 𝙵𝙸𝙻𝙴𝚂.𝙸𝙵 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝙰𝙳𝙳 𝙵𝙸𝙻𝙴𝚂 𝙵𝚁𝙾𝙼 𝙰 𝙿𝚄𝙱𝙻𝙸𝙲 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝙵𝙸𝙻𝚆 𝙻𝙸𝙽𝙺 𝙾𝙽𝙻𝚈  𝙾𝚁 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝙰𝙳𝙳 𝙵𝙸𝙻𝙴𝚂 𝙵𝚁𝙾𝙼 𝙰  𝙿𝚁𝙸𝚅𝙰𝚃𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚈𝙾𝚄 𝙼𝚄𝚂𝚃 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽 𝙾𝙽 𝚃𝙷𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝙰𝙲𝙲𝙴𝚂𝚂 𝙵𝙸𝙻𝙴𝚂...//</b>

⪼ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞 ›

➪ /plink ›› <b>𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰𝙽𝚈 𝙼𝙴𝙳𝙸𝙰 𝚃𝙾 𝙶𝙴𝚃 𝙻𝙸𝙽𝙺.</b>
➪ /pbatch ›› <b>𝚄𝚂𝙴 𝚈𝙾𝚄𝚁 𝙼𝙴𝙳𝙸𝙰 𝙻𝙸𝙽𝙺 𝚆𝙸𝚃𝙷 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳.</b>
➪ /batch ›› <b>𝚃𝙾 𝙲𝚁𝙴𝙰𝚃𝙴 𝙻𝙸𝙽𝙺 𝙵𝙾𝚁 𝙼𝚄𝙻𝚃𝙸𝙿𝙻𝙴 𝙵𝙸𝙻𝙴𝚂.</b>

⪼ 𝐄𝐱𝐚𝐦𝐩𝐥𝐞 ›

<code>/batch https://t.me/gjcjknxz/2 https://t.me/jfksucxhb/8</code>"""

    FORCESUB_TXT = """⚠️ Join our updated channel below.  bot will not give you movie until you join from our update channel...

⚠️ கீழே உள்ள எங்கள் புதுப்பிக்கப்பட்ட சேனலில் சேரவும்.  எங்கள் புதுப்பிப்பு சேனலில் நீங்கள் சேரும் வரை போட் உங்களுக்கு திரைப்படத்தை வழங்காது... 

⚠️ ਹੇਠਾਂ ਸਾਡੇ ਅਪਡੇਟ ਕੀਤੇ ਚੈਨਲ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ।  ਬੋਟ ਤੁਹਾਨੂੰ ਉਦੋਂ ਤੱਕ ਮੂਵੀ ਨਹੀਂ ਦੇਵੇਗਾ ਜਦੋਂ ਤੱਕ ਤੁਸੀਂ ਸਾਡੇ ਅਪਡੇਟ ਚੈਨਲ ਤੋਂ ਸ਼ਾਮਲ ਨਹੀਂ ਹੋ ਜਾਂਦੇ...

⚠️ ചുവടെയുള്ള ഞങ്ങളുടെ അപ്‌ഡേറ്റ് ചെയ്‌ത ചാനലിൽ ചേരുക.  ഞങ്ങളുടെ അപ്‌ഡേറ്റ് ചാനലിൽ നിന്ന് നിങ്ങൾ ചേരുന്നത് വരെ ബോട്ട് നിങ്ങൾക്ക് സിനിമ നൽകില്ല....

⚠️ हमारे निचे दिए गये update चैनल को join करे जब तक आप हमारे update चैनल को join नहीं करेंगे तब तक bot आपको मूवी नहीं देगा...👇👇 join new 👇👇"""

    OWNER_TXT = """<b>
🔹 ᴍʏ ɴᴀᴍᴇ : ᴀᴋꜱʜᴀʏ ᴄʜᴀɴᴅ
🔹 ᴜsᴇʀɴᴀᴍᴇ: @AkshayChand10
🔹 ᴘᴍᴛ. ᴅᴍ ʟɪɴᴋ: <a href=https://t.me/AkshayChand10>ᴀᴋꜱʜᴀʏ ᴄʜᴀɴᴅ</a>
🔹 ᴘʟᴀᴄᴇ:| ᴍᴀʜᴀʀᴀꜱʜᴛʀᴀ | ɪɴᴅɪᴀ
🔹 ᴋɴᴏᴡ ʟᴀɴɢᴜᴀɢᴇ: ʜɪɴᴅɪ, ᴇɴɢʟɪꜱʜ
🔹 ʀᴇʟɪɢɪᴏɴ ᴄᴀsᴛ: ʜɪɴᴅᴜ
🔹 ᴅᴏʙ: 00 | 04 | 2004
🔹 Aɢᴇ: ᴊᴜsᴛ ᴄᴀʟᴄᴜʟᴀᴛᴇ
🔹 ʟᴇᴠᴇʟ: ғʀɪsᴛ ʏᴇᴀʀ ʙᴛᴇᴄ ᴇᴄᴇ
🔹 ғᴀᴠ ᴄᴏʟᴏᴜʀ: ʙʟᴀᴄᴋ, ʀᴇᴅ, ɢʀᴇᴇɴ, ʙʟᴜᴇ..</b>"""
    GROUP_R_TXT = """<b>GROUP RULES

☀️  Search With Correct Spelling..

☀️ Try to Search movie web series With  Year If The bot is Not Sending You Accurate Result..

☀️ Search Series In The Given From Example : Gotham S03E01 And S03E10..

☀️ Search Movies and web series  in The Given From Example:    

🔰 Movies 

(1) Avengers.. ✅
(2) Avengers Hindi..✅
(3) Avengers 2012 Hindi..✅
(4) Don't Tipe Avengers Hindi Dubbed..❌
(5) Avengers Hindi movie..❌

🔰 Web Series

(1) Money heist..✅
(2) Money heist S01 EP1..✅
(3) Money heist Hindi..✅
(4) Money heist all season..❌
(5) Money heist all Hindi season..❌

☀️Don't Do Any Self Promotion.

☀️ Don't Send Any Kind Of Photo Video Documents URL ETC.

☀️ Sending The Above  Mantained Things Will Lead To Permanent Ban.

☀️Don't Request Any Things Other Than Movie Series Animes.

☀️ Give and Tak Respect</b>.."""

MALIK_PHH = """<b>Hay 👋 {}.... 🌷 ❤️

😎 welcome to Our Group...
  
      👉 <s>{}</s> 👈 

😎 You Can Find 🔍 Movies / Series / Animes etc. From Here. Enjoy 😉...

If you have any question then contact us below  👇</b>"""

ALURT_FND = """<b>.

CHECK YOUR MOVIE ON THE GIVEN LIST AND SELECT YOUR MOVIE..</b>"""

ADG = """<b>Hay. {}..\n\nThankyou For Adding Me In.. ❣️

             👉 <s>{}</s> 👈 

If you have any questions & doubts about using me..\n\n Contact my Owner >> @AkshayChand10</b>"""

ADDG = """<b>Hay {},

I'm ⚡️ Powerful Auto-Filter Bot...
😎 You Can Use Me As A Auto-filter in Your Group ....
Its Easy To Use Me; Just Add Me To Your Group As Admin, Thats All, i will Provide Movies There...😎
⚠️ More Help Check Help Button Below

©️Mantained Bʏ  @AkshayChand10</b>"""

M_NT_FND = """<b>⭕️ This Movie Not Found my Database. Request to admin..\n\n⭕️ Ye movie Hamare database me Available nahi hai Niche admin se request kare... \n\n⭕️ Request to admin.. 👇</b>"""



