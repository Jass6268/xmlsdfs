from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_MESSAGE = '''**Hello, {}
I Am "Shareus Demo Bot" , Bulk Link Converter. I Can Convert Links Directly From Your earnbylinks.com Account,
    
1. Go To 👉 https://earnbylinks.com/member/tools/api  
2. Than Copy API Key
3. Than Type /api than give a single space and than paste your API Key (see example to understand more...)**

**/api(space)API Key 
(See Example.👇)
Example:** `/api de303d5270f481aec928f39883da7b7f9a8812ac `

**➕ Hit** 👉 /Features To Know More Features Of This Bot.
**💁‍♀️ Hit** 👉 /help To Get Help.
**➕ Hit** 👉 /channel Command To Get Help About Adding your channel to bot.
**➕ Hit** 👉 /footer To Get Help About Adding your Custom Footer to bot.

 if you want to make this way our url shortener website bot so , contact him :-> @HBMoviesGod .....
'''


HELP_MESSAGE = '''
**Hello, {}
I Am Bulk Link Converter Bot. I Can Convert Links Directly From Your earnbylinks.com Account,**
    
1. Go To 👉 https://earnbylinks.com/member/tools/api  
2. Than **Copy API** Key
3. Than Type **/api** than give a **single space** and than **paste** your **API** Key (**see example** to understand more...)

**/api(space)API Key 
(See Example.👇)
Example:** `/api de303d5270f481aec928f39883da7b7f9a8812ac `

**➕ Hit** 👉 /Features To Know More Features Of This Bot.
**💁‍♀️ Hit** 👉 /help To Get Help.
**➕ Hit** 👉 /channel Command To Get Help About Adding your channel to bot.
**➕ Hit** 👉 /footer To Get Help About Adding your Custom Footer to bot.

If You Want Any **Other Shortner** Link Converter Bot Instead Of earnbylinks.com** than **contact** at 👉 @HBMoviesGod (all **shortners support** available.)**'''


ABOUT_TEXT = """
**Hey! My name is 'Shareus Demo Bot'. 'I am add your url shortener bot earnbylinks.com .**'

**⚡Features⚡**

• I can **Convert any** links or posts to your **domain.com** link / post. (Button Links Posts, Hidden links/Hyperlinks All Are Supported)

• I Can **auto** add custom **footer text** to your every post. Hit 👉 /footer To know more...

• I Can **auto** add custom **Header text** to your every post. Hit 👉 /Header To know more...

• I Can **replace / remove** other's **channel links** with **your channel** link. Hit 👉 /channel To know More...

• I Can **Automatically Replace** Your ***Banner** Image To images in the post. Hit  👉/Banner To Know More... 

• **No** need to share **password or email** to convert links.**


**Click On Custom Alias To Create Custom Link**
"""

CUSTOM_ALIAS_MESSAGE = """For Custom Alias, `[link] | [custom_alias]`, Send in this format

This feature works only in private mode only

Ex: https://t.me/HBMoviesGod | domain.com
"""


ADMINS_MESSAGE = """
List of Admins who has access to this Bot

{admin_list}
"""


CHANNELS_LIST_MESSAGE = """
List of channels that have access to this Bot:

{channels}"""


HELP_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Custom Alias', callback_data=f'alias_conf'),
        InlineKeyboardButton('Admins', callback_data=f'admins_list'),    
    ],

    [
        
        InlineKeyboardButton('Home', callback_data='start_command')
        
    ],


])


ABOUT_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Home', callback_data=f'start_command'),
        InlineKeyboardButton('Help', callback_data=f'help_command')
    ],
    [
        InlineKeyboardButton('Close', callback_data='delete')
    ]
])

START_MESSAGE_REPLY_MARKUP  = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Help', callback_data=f'help_command'),
        InlineKeyboardButton('About', callback_data='about_command')
    ],
        [
        InlineKeyboardButton('Close', callback_data='delete')
    ],

])

METHOD_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Back', callback_data=f'help_command'),
        InlineKeyboardButton('Close', callback_data='delete')
    ],

])

BACK_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Back', callback_data=f'help_command')
    ],

])

USER_ABOUT_MESSAGE = """
- Shortener Website: {base_site}

- {base_site} API: {shortener_api}

- Username: @{username}

- Header Text: 
{header_text}

- Footer Text: 
{footer_text}

- Banner Image: {banner_image}
"""


SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, 
`/api [api]`
            
Ex: `/api 6LZq851sXofffPHugiKQq`

Current Website: {base_site}

Current Shortener API: `{shortener_api}`"""

HEADER_MESSAGE = """Reply to the Header Text You Want

This Text will be added to the top of every message caption or text

For adding line break use \\n

To Remove Header Text: `/header remove`"""

FOOTER_MESSAGE = """Reply to the Footer Text You Want

This Text will be added to the bottom of every message caption or text

For adding line break use \\n

To Remove Footer Text: `/footer remove`"""

USERNAME_TEXT = """**Hello {username}, I am Bulk Link Converter Bot From Linked url shortener bot name Account,**

**🌟 Type** /channel (channel link or username)

**example:**
/channel Username
Or
/channel https://t.me/Username

**🤘 Hit** 👉 /features To Know More Features Of This Bot.**"""

BANNER_IMAGE = """
Usage: `/banner_image image_url` or reply to any Image with this command

This image will be automatically replaced with other images in the post

To remove custom image, `/banner_image remove`

Eg: `/banner_image https://www.nicepng.com/png/detail/436-4369539_movie-logo-film.png`"""

INCLUDE_DOMAIN_TEXT = """
Use this option if you want to short only links from the following domains list.

Current Include Domain:
{}
Usage: /include_domain domain
Ex: `/include_domain t.me, stack.com`

To remove a domain,
Ex: `/include_domain remove t.me`

To remove all domains,
Ex: `/include_domain remove_all`
"""

EXCLUDE_DOMAIN_TEXT = """
Use this option if you wish to short every link on your channel but exclude only the links from the following domains list

Current Exclude Domains:
{}
Usage: /exclude_domain domain
Ex: `/exclude_domain t.me, google.com`

To remove a domain, 
Ex: `/exclude_domain remove t.me`

To remove all domains,
Ex: `/exclude_domain remove_all`
"""

BANNED_USER_TXT = """
Usage: `/ban [User ID]`
Usage: `/unban [User ID]`

List of users that are banned:

{users}
"""
