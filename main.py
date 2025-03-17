import asyncio
import json
import sys

from googletrans import Translator


async def translate_text(srcText: str = "Hello"):
    async with Translator() as translator:
        detected_language = await translator.detect(srcText)
        dest_language = 'en' if detected_language.lang == 'ja' else 'ja'
        result = await translator.translate(srcText, dest=dest_language)
        srcText = result.extra_data['translation'][0][1]
        destText = result.text
        result = {
            "src": result.src,
            "srcText": srcText,
            "dest": result.dest,
            "destText": destText
        }
    
        return {
            'title': f'{srcText} → {destText}',
            'subtitle': f'{result["src"]} → {result["dest"]}',
            'arg': f'{srcText}: {destText}',
            'icon': {
                'type': 'png',
                'path': ''
            }
        }

if __name__ == '__main__':
    search_query = sys.argv[1]
    result = asyncio.run(translate_text(search_query))
    print(json.dumps({"items": [result]}, ensure_ascii=False))

